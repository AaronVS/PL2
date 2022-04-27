#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 22/04/2022

@author: vsaar
"""



from funciones import *

# Path: populate.py

#GENERACIÓN DE DATOS PARA LOS FICHEROS .CSV
# Tener en cuenta la posible alta duración a la hora de generar grandes cantidades en estas funciones como es el caso

# Hay que seguir un orden de ejecución para generar estos datos, si se sigue y se ejecuta todo tal y como está, el funcionamiento debería ser óptimo (aunque largo)

generar_universidades(100000)
generar_estudiantes(5000000, 1)
generar_asignaturas()
generar_estancia()
generar_convalidaciones()

