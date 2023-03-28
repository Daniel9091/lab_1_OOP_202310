# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# librerias
import csv

# funciones
# parte 1
def import_data():
    archive= input("Escriba el nombre del archivo: ")
    if archive =='':
        archive = 'data.csv'
    with open(archive , mode = "r") as csv_file:
        line = csv.DictReader(csv_file, delimiter = ";")
        data = list(line)
        return data


# parte 2
def export_tables_by_region(data, filename):
    n_region ={}
    for line in data:
        if not (line['RegiÃ³n'] in n_region):
            n_region[line['RegiÃ³n']] = 1
        else:
            n_region[line['RegiÃ³n']] +=1
    
    # escritura de nuevo archivo
    reporte =  open(filename,'w')
    for region in n_region:
        reporte.write(region +':    ' + str(n_region[region]) + '\n')
    reporte.close()


# parte 3
def export_general_results(data, filename):
    recuento = {}
    for line in data:
        if not (line['Candidato'] in recuento ):
            recuento[line['Candidato']] =   int(line['Votos TRICEL'])
        else:
            recuento[line['Candidato']] +=  int(line['Votos TRICEL'])
    
    # escritura del exel con los resultados finales de las votaciones
    results = open(filename,'w')
    for candidato in recuento:
        results.write(candidato +':    ' + str(recuento[candidato]) + '\n')
    results.close()


# parte 4
def export_count_by_local(data,filename):
    local = input('ingrese un local para el conteo: ')
    if local =='':
        local ='COLEGIO CATOLICO NAZARET' # colegio por defaut para probar mas rapido el programa
    # ANEXO DE COLEGIO SAN ANTONIO DE MATILLA   
    # COLEGIO CATOLICO NAZARET
    
    voto = {}
    for line in data:
        if line['Local'] == local:
            if not (line['Candidato'] in voto):
                voto[line['Candidato']] = int(line['Votos TRICEL'])
            else:
                voto[line['Candidato']] += int(line['Votos TRICEL'])
    
    # escritura de texto que contiene el conteo de datos por local
    c_for_local = open(filename,'w')
    c_for_local.write(local + '\n')
    for candidato in voto:
        c_for_local.write(candidato + ':    ' + str(voto[candidato]) + '\n')
    c_for_local.close()
            
     



# inicio programa
data = import_data()
filename_r= input('ingrese nombre del reporte: ')   # filname_r: el nombre del archivo reporte
if filename_r =='':
    filename_r = 'Report.txt'
    
export_tables_by_region(data, filename_r)


filename_t = input('ingrese nombre del exel con los resultados: ')   # filname_t: el nombre del archivo result (t de total)
if filename_t =='':
    filename_t = 'Results.csv'

export_general_results(data, filename_t)

filename_cl = input('ingrese el nombre del archivo resumen del conteo por local de votos: ')
if filename_cl =='':
    filename_cl = 'Conteo de votos por local.txt'

export_count_by_local(data,filename_cl)
 


        
 
    












