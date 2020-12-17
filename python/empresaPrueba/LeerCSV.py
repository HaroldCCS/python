# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:27:20 2020

@author: Harold
"""


import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('Prueba.csv',header=0)

df=pd.DataFrame(datos)

 # datos punto 2 reportados
reportados = pd.DataFrame(df.iloc[:,[1,3]])
sector1 = reportados.loc[:, 'Sector'] == 'Sector 1'
df_sector1 = df.loc[sector1]
TotalSector1 = df_sector1['Reportados'].sum()

sector2 = reportados.loc[:, 'Sector'] == 'Sector 2'
df_sector2 = df.loc[sector2]
TotalSector2 = df_sector2['Reportados'].sum()

sector3 = reportados.loc[:, 'Sector'] == 'Sector 3'
df_sector3 = df.loc[sector3]
TotalSector3 = df_sector3['Reportados'].sum()

sector4 = reportados.loc[:, 'Sector'] == 'Sector 4'
df_sector4 = df.loc[sector4]
TotalSector4 = df_sector4['Reportados'].sum()

sector5 = reportados.loc[:, 'Sector'] == 'Sector 5'
df_sector5 = df.loc[sector5]
TotalSector5 = df_sector5['Reportados'].sum()


df_grafica_reportados = (TotalSector1, TotalSector2, TotalSector3, TotalSector4, TotalSector5)
df_grafica_nombres=('Sector 1','Sector 2','Sector 3','Sector 4','Sector 5')


plt.pie(df_grafica_reportados, labels=df_grafica_nombres , autopct='%1.1f%%')
plt.title("Reportados por sector", weight ='bold', size = 14)
plt.savefig(str("Reportados_Por_Sectores")+'.png', dpi=100, bbox_inches="tight")
plt.show()



 # datos punto 3 validadaos

validados = pd.DataFrame(df.iloc[:,[1,4]])


sector1 = validados.loc[:, 'Sector'] == 'Sector 1'
df_sector1 = df.loc[sector1]
TotalSector1 = df_sector1['Validos'].sum()

sector2 = validados.loc[:, 'Sector'] == 'Sector 2'
df_sector2 = df.loc[sector2]
TotalSector2 = df_sector2['Validos'].sum()

sector3 = validados.loc[:, 'Sector'] == 'Sector 3'
df_sector3 = df.loc[sector3]
TotalSector3 = df_sector3['Validos'].sum()

sector4 = validados.loc[:, 'Sector'] == 'Sector 4'
df_sector4 = df.loc[sector4]
TotalSector4 = df_sector4['Validos'].sum()

sector5 = validados.loc[:, 'Sector'] == 'Sector 5'
df_sector5 = df.loc[sector5]
TotalSector5 = df_sector5['Validos'].sum()


df_grafica_validados = (TotalSector1, TotalSector2, TotalSector3, TotalSector4, TotalSector5)


plt.pie(df_grafica_validados, labels=df_grafica_nombres , autopct='%1.1f%%')
plt.title("Validados por sector", weight ='bold', size = 14)
plt.savefig(str("validados_Por_Sectores")+'.png', dpi=100, bbox_inches="tight")
plt.show()


 # datos punto 4 rechazadoss
vrechazados =  pd.DataFrame(df.iloc[:,[1,5]])


sector1 = vrechazados.loc[:, 'Sector'] == 'Sector 1'
df_sector1 = df.loc[sector1]
TotalSector1 = df_sector1['Rechazados'].sum()

sector2 = vrechazados.loc[:, 'Sector'] == 'Sector 2'
df_sector2 = df.loc[sector2]
TotalSector2 = df_sector2['Rechazados'].sum()

sector3 = vrechazados.loc[:, 'Sector'] == 'Sector 3'
df_sector3 = df.loc[sector3]
TotalSector3 = df_sector3['Rechazados'].sum()

sector4 = vrechazados.loc[:, 'Sector'] == 'Sector 4'
df_sector4 = df.loc[sector4]
TotalSector4 = df_sector4['Rechazados'].sum()

sector5 = vrechazados.loc[:, 'Sector'] == 'Sector 5'
df_sector5 = df.loc[sector5]
TotalSector5 = df_sector5['Rechazados'].sum()


df_grafica_vrechazados = (TotalSector1, TotalSector2, TotalSector3, TotalSector4, TotalSector5)


plt.pie(df_grafica_vrechazados, labels=df_grafica_nombres , autopct='%1.1f%%')
plt.title("rechazados por sector", weight ='bold', size = 14)
plt.savefig(str("rechazados_Por_Sectores")+'.png', dpi=100, bbox_inches="tight")
plt.show()
