# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

matriz=[[1,2,3],[4,5,6],[7,8,9]]
aux=1
i=0
j=0
cont=0
while aux != 0:
    
    
    
    if i==0 and j!=2:
        
        print(matriz[i][j])
        j+=1
   
    if j==2 and i!=2:
        
        print(matriz[i][j])
        i+=1
       
    if i==2 and j!=0:
        print(matriz[i][j])
        j-=1
    if j==0 and i==2:
        print(matriz[i][j])
        i-=1
    if j==0 and i!=2:
        print(matriz[i][j])
        j+=1
    if i==j:
        print(matriz[i][j])
        aux=0
    
    