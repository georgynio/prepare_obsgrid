# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:17:04 2016

@author: Ragy
"""

'''
Este script ordena los datos de las estaciones en un unico archivo de tipo reporte, 
disponible para rodar el OBSGRID
'''

import pandas as pd

dir1='/dados_obsgrid/' # endereço do arquivo da variavel
arq1='dados_2010-arquvio_completo_correto.xls' # nome do arquivo das estações
arq2='vix_airport.xlsx' # nome do arquivo do aeroporto (monitoramento)

book=pd.ExcelFile(dir1+arq1)
book2=pd.ExcelFile(dir1+arq2)

hoja=book.parse('dados') # nome da aba onde que estão os dados monitorados
hoja2=book2.parse('Dados Aeroporto') # nome da aba onde que estão os dados monitorados

la1=hoja2.shape 
#for i in range(la1[0]):
#    for j in range(la1[1]):
#        if hoja2.iloc[i,j]:
#            hoja2.iloc[i,j]=-777777
#    
# estacao
e=[] # matriz nula para designar o nnumero da estação
#e.append('E0') # carapina
#e.append('E1') # enseada do sua
#e.append('E2') # ibes
#e.append('E3') # cariacica
e.append('E4') # aeropuerto

lat_est=[]
lon_est=[]
#lat_est.append(-20.22769)
#lon_est.append(-40.25641)
#lat_est.append(-20.31333)
#lon_est.append(-40.29063)
#lat_est.append(-20.34844)
#lon_est.append(-40.31733)
#lat_est.append(-20.34114)
#lon_est.append(-40.40199)
lat_est.append(-20.25117)
lon_est.append(-40.28540)

n=[] # matriz nula para designar o nome da estação
#n.append('carapina')
#n.append('enseada do sua')
#n.append('ibes')
#n.append('cariacica')
n.append('aeropuerto')

# elevacion
#el.append(23)
#el.append(6)
#el.append(13)
#el.append(18)
el=9

# presion
#[7:8768]
#p_cara=hoja.icol(25) # carapina
#p_sua= -777777 # enseada do sua
#p_ibe= -777777 # ibes
#p_cari= -777777 # cariacica
p_aero=hoja2.iloc[:,7] #aeropuerto

# altura de medicion
#h_cara= 23 # carapina
#h_sua= 6 # enseada do sua
#h_ibe= 13 # ibes
#h_cari= 18 # cariacica
h_aero= 9 #aeropuerto

# temperatura
#t_cara=hoja.icol(21) # carapina
#t_sua= -777777 # enseada do sua
#t_ibe= -777777 # ibes
#t_cari=hoja.icol(107) # cariacica
t_aero=hoja2.iloc[:,8] #aeropuerto

# punto de rocio
#r_cara=hoja.icol(17) # carapina
#r_sua= -777777 # enseada do sua
#r_ibe= -777777 # ibes
#r_cari= -777777 # cariacica
r_aero=hoja2.iloc[:,9] #aeropuerto

# velocidad
#vel.append([]),vel[0].append(hoja.icol(17)[7:]) # carapina
#vel.append([]),vel[1].append(hoja.icol(53)[7:]) # enseada do sua
#vel.append([]),vel[2].append(hoja.icol(83)[7:]) # ibes
#vel.append([]),vel[3].append(hoja.icol(103)[7:]) # cariacica
vel=hoja2.iloc[:,3] #aeropuerto


# direccion
#d_cara=hoja.icol(19) # carapina
#d_sua=hoja.icol(55)  # enseada do sua
#d_ibe=hoja.icol(85)  # ibes
#d_cari= -777777 # cariacica
d_aero=hoja2.iloc[:,2] #aeropuerto

# humedad
#u_cara=hoja.icol(23) # carapina
#u_sua= -777777 # enseada do sua
#u_ibe= -777777 # ibes
#u_cari=hoja.icol(109)# cariacica
u_aero= -777777 #aeropuerto

#la=hoja.shape
#la[0]
#for i in range(7,la[0]):
#    for j in range(la[1]):
#        if hoja.iloc[i,j]:
#            hoja.iloc[i,j]=-777777



days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1,13):
    ic=sum(days[:i-1])*24 # te coloca no inicio da coluna a ser trabalhada
    ic1=sum(days[:i])*24 # te coloca no final da coluna a ser trabalhada
    dia=0
    for k in range(ic,ic1,24):
        dia+=1
        for m in range(0,24,3):
            f=open('nuevo_OBS/'+'OBS%3A2010'+'-%02d'%i+'-%02d'%dia+'_%02d'%(m),'w') # abrir um arquivo com o nome xxx
            for l in range(3):
                print >>f, ('''{0:20.5f}{1:20.5f}{2:40s}{3:40s}{4:40s}{5:40s}{6:20.5f}{7:10d}{8:10d}{9:10d}{10:10d}{11:10d}\
{12:10s}{13:10s}{14:10s}{15:10d}{16:10d}{17:20s}{18:13.5f}{19:7d}{20:13.5f}{21:7d}{22:13.5f}{23:7d}{24:13.5f}{25:7d}\
{26:13.5f}{27:7d}{28:13.5f}{29:7d}{30:13.5f}{31:7d}{32:13.5f}{33:7d}{34:13.5f}{35:7d}{36:13.5f}{37:7d}\
{38:13.5f}{39:7d}{40:13.5f}{41:7d}{42:13.5f}{43:7d}'''.format(lat_est[0],lon_est[0],e[0],n[0],
                'Dados meteorologicos superficiais','NQUALIAR',el,6,0,0,0,0,'F','T','F',-888888,-888888,
                '2010'+'%02d'%i+'%02d'%dia+'%02d'%(m+l)+'0000',100000,0,-888888,0,-888888,0,-888888,0,-888888,0,-888888,0,
                -888888,0,-888888,0,-888888,0,-888888,0,-888888,0,-888888,0,-888888,0))
                 
                print >>f, ('''{0:13.5f}{1:7d}{2:13.5f}{3:7d}{4:13.5f}{5:7d}{6:13.5f}{7:7d}{8:13.5f}{9:7d}{10:13.5f}{11:7d}\
{12:13.5f}{13:7d}{14:13.5f}{15:7d}{16:13.5f}{17:7d}{18:13.5f}{19:7d}'''.format(p_aero[k+m+l],0,10,0,
                t_aero[k+m+l],0,r_aero[k+m+l],0,vel[k+m+l],0,d_aero[k+m+l],0,-888888,0,-888888,0,-888888,0,-888888,0))
                print >>f, ('''{0:13.5f}{1:7d}{2:13.5f}{3:7d}{4:13.5f}{5:7d}{6:13.5f}{7:7d}{8:13.5f}{9:7d}{10:13.5f}{11:7d}\
{12:13.5f}{13:7d}{14:13.5f}{15:7d}{16:13.5f}{17:7d}{18:13.5f}{19:7d}'''.format(-777777,0,-777777,0,1,0,-888888,0,-888888,
                0,-888888,0,-888888,0,-888888,0,-888888,0,-888888,0))
                print >>f, ('{0:7d}{1:7d}{2:7d}'.format(6,0,0))

            f.close()
