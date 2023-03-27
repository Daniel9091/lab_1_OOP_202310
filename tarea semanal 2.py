# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:29:59 2023

@author: xdfytfcacer
"""

# tarea paradigmas de la programacion
# parte 1
# correspondienrte a la funcion import_data()


def import_data():
    # listas
    l_lin   = []
    keys    = []
    # diccionarios
    datos   = {}
    
    # pregunta nombre del archivo
    name_archive = input('Ingrese el nombre del archivo que va a abrir: ')
    if name_archive == '':
        name_archive = 'data.csv'
    
    # exporta datos  
    base = open(name_archive)
    
    # lector del archivo completo
    line1 = base.readline()
    # lista de lista que contiene todos los datos del archivo, sin las claves 
    for line in base:
        l_lin.append((base.readline()).split(';')) 
    
    # preparacion de key
    keys = line1.split(';')
    # combiercion de l_lin (list of list) a datos (dic de list)
    for i in range(len(keys)):
        dato = []
        for i2 in range(len(l_lin)):
            dato.append(l_lin[i2][i])
        datos[keys[i]] = dato
    return datos

# inicio programa

data = import_data()
    
    














