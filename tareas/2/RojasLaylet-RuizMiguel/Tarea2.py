# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y94QT8rSh5p54Vgf-Fk5dD117nvEJz4f
"""

import os
import sys
import time
import datetime

def principal():
    if len(sys.argv) != 3: 
        print("Error: El programa requiere la ruta del directorio y el número de días.")
        print("Invocación: directorio.py <ruta_directorio> <número_días>")
        return

    #Obtenemos ruta y días
    ruta_directorio = sys.argv[1]
    dias = sys.argv[2]

    if not os.path.isdir(ruta_directorio):
        print("Error: El directorio seleccionado no existe.")
        return

    print("Nombre                                                            Última Modificación   Modo  Tamaño")
    print("=" * 100)
    
    # Obtener la fecha actual en segundos desde el local
    fecha_hoy = time.time()
    # Ordenar los nombres de los archivos alfabéticamente
    archivos = sorted(os.listdir(ruta_directorio))

    #Recorremos los archivos 

    for archivo in os.listdir(ruta_directorio):
        ruta= os.path.join(ruta_directorio, archivo)
        if os.path.isfile(ruta):
            ultima_modificacion = os.path.getmtime(ruta)
            #3600(seg*h)*24(horas en un día)= 86400
            diferencia_dias= (fecha_hoy - ultima_modificacion) / 86400
            #Vemos si entra en el rango de días permitidos
            if diferencia_dias <= int(dias):
                obtener_propiedades(ruta) 


def obtener_propiedades(ruta_directorio):
    nombre = nombre = os.path.basename(ruta_directorio)
    tamaño = os.path.getsize(ruta_directorio)
    # Convertir la fecha de modificación a un formato legible
    file_mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(ruta_directorio)))
    #Permisos de el archivo
    modo = oct(os.stat(ruta_directorio).st_mode)[3:]

    print(f'{nombre:70} {file_mtime:16} {modo} {tamaño}')


principal()