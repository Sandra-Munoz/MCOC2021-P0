# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import matmul, rand
from time import perf_counter
from numpy.linalg import inv, eigh 
from numpy import eye, double, ones

Ns=[10,100,1000,2000,2000,4000,5000,6000,7000,8000]
Dts=[]
fid=open("A I Double rendimiento.txt ","w")

for i in range(10):
    Dts=[]
    def matriz_laplaciana(N,t=double):
        e=eye(N)-eye(N,N,1)
        return t(e+e.T)

    for N in Ns:
        A=matriz_laplaciana(N)
        b=ones(N)
        t1=perf_counter()
        x=inv(A)*b
        t2=perf_counter()
        
        dt=t2-t1
        
        Dts.append(dt)
        
        print(f"N={N} dt={dt} s")
    
        fid.write(f"{N} {dt}\n")

fid.close()
