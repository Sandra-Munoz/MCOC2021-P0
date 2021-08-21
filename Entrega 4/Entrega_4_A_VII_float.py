# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:16:29 2021

@author: sandra
"""

from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import inv, eigh, solve
from numpy import eye, float32, ones

Ns=[10,100,1000,2000,2000,4000,5000,6000,7000,8000]
Dts=[]
fid=open("A VII Float rendimiento.txt ","w")

for i in range(10):
    Dts=[]
    def matriz_laplaciana(N,t=float32):
        e=eye(N)-eye(N,N,1)
        return t(e+e.T)

    for N in Ns:
        A=matriz_laplaciana(N)
        b=ones(N)
        t1=perf_counter()
        x=solve(A,b,overwrite_a=True,overwrite_b=True)
        t2=perf_counter()
        
        dt=t2-t1
        
        Dts.append(dt)
        
        print(f"N={N} dt={dt} s")
    
        fid.write(f"{N} {dt}\n")

fid.close()