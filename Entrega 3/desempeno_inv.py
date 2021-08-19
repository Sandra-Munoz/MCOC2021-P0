# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from time import perf_counter
from numpy.linalg import inv 
from laplaciana import laplaciana 
from numpy import half, single, double, longdouble, eye, zeros

def matriz_laplaciana(N,t=double):
    e=eye(N)-eye(N,N,1)
    return t(e+e.T)

N=2500

t1=perf_counter()
A=matriz_laplaciana(N,t=double)
t2=perf_counter()
Am1=inv(A)
t3=perf_counter()

dt_ensamblaje=t2-t1
dt_inversion=t3-t2

bytes_total=A.nbytes+Am1.nbytes

print(f"Uso memoria:{bytes_total} bytes")

#print(f"tiempo ensamblaje:{dt_ensamblaje} s")

#print(f"tiempo inversion:{dt_inversion} s")


