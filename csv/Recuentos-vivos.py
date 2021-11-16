import os
import csv 
import pprint
import pandas as pd


ruta = "C:/Users/avpen/Desktop/mi-git/Curso21-22-main/csv/"

#leer archivo diccionario

# def leer_titanic():
#     csv_in =open(ruta + 'titanic.csv')
#     lector_dic = csv.DictReader(csv_in)
    
#     lista_dic = list(lector_dic)

#     csv_in.close
#     return lista_dic

# pprint.pprint(leer_titanic())



def contador():
    df = pd.read_csv(ruta + 'titanic.csv')
    survived = df['Survived']

    vivos = 0

    muertos = 0

    for s in survived:
        if s == 1:
            vivos += 1
        else:
            muertos += 1
    return vivos,muertos

v,m = contador()
vivos = v
muertos = m
print('Vivieron:')
print(v)
print('Murieron:')
print(m)
