# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:27:20 2020
@author: Harold
"""


import pandas as pd
import matplotlib.pyplot as plt

# datos punto 1 Leer csv
datos = pd.read_csv('Prueba.csv',header=0)

df=pd.DataFrame(datos)

grafica_nombres=('Sector 1','Sector 2','Sector 3','Sector 4','Sector 5')

def procesar_datos(columna):
    datos = df[['Sector',columna]]
    
    datos_grafica = []
    
    i = 1
    while (i < 6):
        nombre = "Sector {}".format(i)
        sector = datos[datos['Sector'] == nombre]
        datos_grafica.append(sector[columna].sum())
        i = i + 1
    
    plt.pie(datos_grafica, labels=grafica_nombres , autopct='%1.1f%%')
    plt.title("{} por sector".format(columna), weight ='bold', size = 14)
    plt.savefig(str("{}_Por_Sectores").format(columna)+'.png', dpi=100, bbox_inches="tight")
    plt.show()


# datos punto 2 Reportados
procesar_datos('Reportados')

# datos punto 3 validos
procesar_datos('Validos')

# datos punto 4 Rechazados
procesar_datos('Rechazados')


# datos punto 5 Entidad con mas Rechazados
rechazados = df[['Entidad','Rechazados']]

entidades = []

i = 1
while( i < 51):
    nombre = "Entidad {}".format(i)
    entidad = rechazados[rechazados['Entidad'] == nombre]
    entidades.append(entidad['Rechazados'].sum())
    i = i + 1
print('La entidad que tuvo mas registros rechazados fue: Entidad ' , 
      (entidades.index(max(entidades))+1))