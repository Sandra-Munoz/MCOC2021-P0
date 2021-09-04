# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:48:40 2021

@author: sandra
"""

from scipy import matmul, rand
from time import perf_counter
from numpy.linalg import inv, eigh, solve
from numpy import eye, double, ones
import scipy.sparse as sparse 

def matriz_laplaciana(N,t=double):
      e=eye(N)-eye(N,N,1)
      return t(e+e.T)


Ns=[10,100,1000,2000,2000,4000,5000,6000,7000,8000]
Dts=[]
Dts2=[]
fid=open("CasoMatrizDispersa-inv.txt ","w")

for i in range(10):
    
    for N in Ns:
       
        t1=perf_counter()
        A=matriz_laplaciana(N)
        b=matriz_laplaciana(N)
        Acsr1=sparse.csr_matrix(A)
        Acsr2=sparse.csr_matrix(b)
        t2=perf_counter()
        x=inv(A)
        t3=perf_counter()
        
        dt=t2-t1 #tiempo ensamblado
        dt2=t3-t2 #tiempo de solución
        Dts.append(dt)
        Dts2.append(dt2)
        
        print(f"N={N} dt={dt} dt2={dt2}")
    
        fid.write(f"{N} {dt} {dt2} \n")


fid.close()

A[0,-1]=1
A[1,-1]=1
A[2,-1]=1
A[3,-1]=1

#print(f"A=\n{A}")
t4=perf_counter()
print(t4)