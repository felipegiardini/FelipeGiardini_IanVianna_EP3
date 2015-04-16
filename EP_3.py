# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:55:13 2015

@author: felipegiardini

"""


#ABRINDO O ARQUIVO CALORIAS
a  = open('usuario.csv', encoding='utf-8')
linhas = a.readlines()

        
#LIMPANDO O ARQUIVO
y = 0
while y < 11  :
    linhas[y] = linhas[y].lower().strip().split(',')
    y+=1
    

#CONFIGURANDO OS DADOS DO USUARIO NO DICIONARIO
linha0 = linhas[0]
linha1 = linhas[1]


dados_usuario = {}
x = 0
while x < 6:
    dados_usuario[linha0[x]]=linha1[x]
    x+=1



#DESCOBRINDO AS CALORIAS NECESSARIAS
idade = float((dados_usuario['idade (anos)']))
peso = float((dados_usuario['peso (kg)']))
altura = float((dados_usuario['altura (m)']))


if dados_usuario['sexo'] == 'm':
    TMBm = ((88.36)+(13.4*peso)+(4.8*altura*100)-(5.7*idade))
    if dados_usuario['fator'] == 'grau minimo':
        k = TMBm*1.2
    if dados_usuario['fator'] == 'baixo':
        k = TMBm*1.375
    if dados_usuario['fator'] == 'medio':
        k = TMBm*1.55
    if dados_usuario['fator'] == 'alto':
        k = TMBm*1.725
    if dados_usuario['fator'] == 'muito alto':
        k = TMBm*1.9
    
    
if dados_usuario['sexo'] == 'f':
    TMBf = 447.6+(9.2*peso)+(3.1*altura*100)-(4.3*idade)
    if dados_usuario['fator'] == 'grau minimo':
        k = TMBf*1.2
    if dados_usuario['fator'] == 'baixo':
        k = TMBf*1.375
    if dados_usuario['fator'] == 'medio':
        k = TMBf*1.55
    if dados_usuario['fator'] == 'alto':
        k = TMBf*1.725
    if dados_usuario['fator'] == 'muito alto':
        k = TMBf*1.9
za = k

#GRAFICO DAS CALORIAS NECESSARIAS
import matplotlib.pyplot as plt
#caloriasnecessarias = [k]*7
#tempo = range(1,8)
#plt.plot(tempo, caloriasnecessarias)
#plt.axis([1,7,0,4000])
#plt.ylabel('calorias (kcal)')
#plt.xlabel('semana')
#plt.title('calorias recomendadas' )
#plt.show()

    

#ABRINDO O ARQUIVO ALIMENTOS
x = open('alimentos.csv', encoding='latin1') 
linhas_alimentos = x.readlines()


#CONFIGURANDO O DICIONARIO DA DIETA DO USUARIO E A DATA
dieta_usuario = {}
data = {}
for i in linhas[3:]:
    pedacos = i
    dieta_usuario[pedacos[1]] = pedacos[2]
    if pedacos[0] in data:
        data[pedacos[0]] += [pedacos[1]]
    else:
        data[pedacos[0]] = [pedacos[1]]
print(data)
print(' ' )
print(dieta_usuario)



#CONFIGURANDO O DICIONARIO DOS ALIMENTOS E SEUS DADOS
alimentos = {}
for e in linhas_alimentos[1:]:
    t = e.strip()
    t = t.lower()
    s = t.split(',')
    pedacos = s
    dados_alimentos = pedacos[1:]
    alimentos[pedacos[0]] = pedacos[1:]
print(' ')
#print(alimentos)





#CONFIGUANDO: CALORIAS, PROTENIAS, CARBOIDRADOS E GORDURAS
k = 0
calorias = []
for e in data.keys():
    for i in data[e]:
        c = float(dieta_usuario[i])*float(alimentos[i][1])/100
        k += c
    calorias.append(k)
    c = 0
    k = 0
print('calorias',calorias)

        
    
    

proteinas = []
k = 0
for e in data.keys():

    for i in data[e]:
        c = float(dieta_usuario[i])*float(alimentos[i][2])/100
        k += c
    proteinas.append(k)
    c = 0
    k = 0
print('proteinhas',proteinas)


carboidratos = []
k = 0
for e in data.keys():

    for i in data[e]:
        c = float(dieta_usuario[i])*float(alimentos[i][3])/100
        k += c
    carboidratos.append(k)
    c = 0
    k = 0
print('carboidrato',carboidratos)


gorduras = []
k = 0
for e in data.keys():

    for i in data[e]:
        c = float(dieta_usuario[i])*float(alimentos[i][4])/100
        k += c
    gorduras.append(k)
    c = 0
    k = 0
print('gorduras',gorduras)



caloriasnecessarias = [za]*2
tempo = range(2)
plt.plot(tempo, caloriasnecessarias)
plt.plot(tempo, calorias)
plt.axis([0,6,0,4000])
plt.ylabel('CALORIAS(Kcal): RECOMENDADAS [AZUL]  X  REAL [VERDE]')
plt.xlabel('semana')
plt.title('calorias recomendadas' )
plt.show()



tempo = range(2)
plt.plot(tempo, proteinas)
plt.plot(tempo, carboidratos)
plt.plot(tempo, gorduras)
plt.axis([0,6,0,200])
plt.ylabel('PROTEINAS[AZUL]- CARBOIDRATOS[VERDE]- GORDURA[VERMELHO]')
plt.xlabel('semana') 
plt.title('quantidade consumida' )
plt.show()
        
    
        

    
       

            
        
    

  

    

 








 