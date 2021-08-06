#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 23:18:57 2021

@author: sandramunozavila
"""

from scipy import matmul, rand 
from numpy import zeros,float16,float32,float64
from time import perf_counter 
import matplotlib.pylab as plt 


Ns=[10,20,50,100,200,500,1000,2000,5000,10000]

Dts=[]
Mems=[]

fid=open("rendimiento.txt ","w")

for i in range(10):
    Dts=[]
    Mems=[]
    for N in Ns:
        A = zeros((N,N),dtype=float32) + 1
        uso_memoeria_teorica=4*N*N
        uso_memoeria_numpy=A.nbytes
       
        #print(f"uso_memoria_teorica = {uso_memoeria_teorica}")
        #print(f"uso_memoria_numpy = {uso_memoeria_numpy}")
        
        B = zeros((N,N))+2
    
        t1=perf_counter()
        C = A@B
        t2 = perf_counter()
        
        uso_memoria_total=A.nbytes+B.nbytes+C.nbytes
    
        dt = t2-t1
        Dts.append(dt)
        Mems.append(uso_memoria_total)
    
        print(f"N={N} dt={dt} s mem={uso_memoria_total}bytes")
    
        fid.write(f"{N} {dt} {uso_memoria_total}\n")

fid.close()