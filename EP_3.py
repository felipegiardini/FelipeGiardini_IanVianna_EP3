# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:55:13 2015

@author: felipegiardini

"""


#ABRINDO O ARQUIVO
a  = open('usuario.csv', encoding='utf-8')
linhas = a.readlines()
for t in linhas:
    print(t)
        
#LIMPANDO O ARQUIVO
y = 0
while y < 11  :
    linhas[y] = linhas[y].lower().strip().split(',')
    y+=1
    

#CONFIGURANDO OS DADOS DO USUARIO NO DICIONARIO
linha0 = linhas[0]
linha1 = linhas[1]
print(linha1)

dados_usuario = {}
x = 0
while x < 6:
    dados_usuario[linha0[x]]=linha1[x]
    x+=1
print(dados_usuario)


#DESCOBRINDO AS CALORIAS NECESSARIAS
idade = float((dados_usuario['idade (anos)']))
peso = float((dados_usuario['peso (kg)']))
altura = float((dados_usuario['altura (m)']))


if dados_usuario['sexo'] == 'm':
    TMBm = ((88.36)+(13.4*peso)+(4.8*altura)-(5.7*idade))
    
    
if dados_usuario['sexo'] == 'f':
    TMBf = 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)
    




    
















#dieta_usuario = {} 
#
#for i in linhas[3:]:
#    pedacos = i
#    print(pedacos[0])

        

    
       

            
        
    

  

    

 








 