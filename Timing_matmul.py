#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 23:33:50 2021

@author: sandramunozavila
"""

from numpy import zeros
from time import perf_counter

N = 1000
A = zeros((N, N)) + 1
B = zeros((N, N)) + 2

t1 = perf_counter()
C = A @ B
t2 = perf_counter()

dt = t2 - t1

print("dt=", dt)