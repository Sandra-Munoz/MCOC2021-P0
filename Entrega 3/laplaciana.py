# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:53:58 2021

@author: sandra
"""
from numpy import zeros 

def laplaciana(N,dtype):
    A=zeros((N,N),dtype=dtype)
    
    for i in range (N):
        A[i,i]=2
        for j in range (max(0,i-2),i):
            if abs(i-j)==1:
                A[i,j]=-1
                A[i,j]=-1
    return A
                