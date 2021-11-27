#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import os
import csv
import sqlite3

import numpy as np

# https://extendsclass.com/sqlite-browser.html


def create_schema():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS sensor;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE sensor(
                [id] INTEGER PRIMARY KEY,
                [pulso] INTEGER NOT NULL
            );
            """)

    conn.commit()
    conn.close()

def show_estadistica():
    # establece conexion a Data Base
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    # Recupera
    pulsos = c.execute("SELECT pulso FROM sensor").fetchall()

    pulsos = np.asanyarray(pulsos)
    if (len(pulsos) > 0):
        print('Pulso Medio ',pulsos.mean())
        print('Pulso Maximo ',pulsos.max())
        print('Pulso Minimo ',pulsos.min())
        print('Pulso Standard ',pulsos.std())


def carga_tabla_desde_csv():
    # Establece conexion a Data Base
     conn = sqlite3.connect('heart.db')
     c = conn.cursor()

    # Define CSV
     path = os.path.dirname(__file__)
     sensor_path = os.path.join(path, 'sensor.csv')

    # Lee CSV
     with open(sensor_path) as fi:
         data = csv.DictReader(fi)

         for row in data:
             pulso = int(row['pulso'])
             if pulso <= 50:
                 continue

            # Carga tabla sensor     
             c.execute("INSERT INTO sensor (pulso) VALUES (?);", [pulso])

    # Cierra Data Base
     conn.commit()
     conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python - Data Base - CSV")

    # Crea Base de datos
    create_schema()
    # Carga datos en tabla desde CSV
    carga_tabla_desde_csv()
    # Muestra estadistica
    show_estadistica()

    print("Fin programa")

