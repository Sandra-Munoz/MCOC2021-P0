# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:44:18 2021

@author: sandra
"""

from time import perf_counter
from numpy.linalg import inv 
from laplaciana import laplaciana 
from numpy import half, single, double, longdouble, eye, zeros

Ns=[10,50,100,1000,2000,2500]
Dts=[]
Mems=[]
fid=open("caso 1 half rendimiento.txt ","w")

for i in range(10):
    Dts=[]
    Mems=[]
    def matriz_laplaciana(N,t=half):
        e=eye(N)-eye(N,N,1)
        return t(e+e.T)

    for N in Ns:
        t1=perf_counter()
        A=matriz_laplaciana(N,t=half)
        t2=perf_counter()
        Am1=inv(A)
        t3=perf_counter()
        
        dt_ensamblaje=t2-t1
        dt_inversion=t3-t2
        
        bytes_total=A.nbytes+Am1.nbytes
        
        Dts.append(dt_inversion)
        Mems.append(bytes_total)
        
        print(f"N={N} dt={dt_inversion} s Memoria={bytes_total} bytes")
    
        fid.write(f"{N} {dt_inversion} {bytes_total}\n")

fid.close()
#print(f"tiempo ensamblaje:{dt_ensamblaje} s")

#print(f"tiempo inversion:{dt_inversion} s")
