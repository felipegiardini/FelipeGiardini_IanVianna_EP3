# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:55:13 2015

@author: felipegiardini
"""



a  = open('usuario.csv', encoding='utf-8')
b = a.readlines()


for i in b:
    h = i.upper()
    k = h.split(',')
    print(k)



x = open('alimentos.csv', encoding='latin1') 
c = x.readlines()

for e in c:
    t = e.upper()
    s = t.split(',')
    print(s) 




 