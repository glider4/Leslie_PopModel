#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:18:44 2019
@author: Mathemacode

This program calculates lambda, which is
x(t+1) / x(t).  L(v) = lambda(v), where L is
the Leslie matrix.

Leslie matrices are commonly used in population
growth / decline problems and the example here has
a few different stages of population, with initial 
population conditions (Y(x, 0)), and declines over 
time.
"""
import numpy as np

n = 150  # number of iterations - more iterations, more decimal accuracy
Y = np.zeros([4,n])  # this is actually frequently referred to as the "x" matrix (results)
lam = np.zeros([4,n])  # a matrix to fill in with the lambda values as it condenses

# Reproduction rates
REP1 = 0
REP2 = 0.2
REP3 = 1.3
REP4 = 3.5

# Survival rates
SURV1 = 0.1
SURV2 = 0.2
SURV3 = 0.36

# Initial population
Y[0,0] = 30000
Y[1,0] = 4500
Y[2,0] = 800
Y[3,0] = 300

# Calculate
for i in range(1,n):
    Y[0,i] = REP1*Y[0, i-1] + REP2*Y[1, i-1] + REP3*Y[2, i-1] + REP4*Y[3, i-1]
    Y[1,i] = SURV1*Y[0, i-1]
    Y[2,i] = SURV2*Y[1, i-1]
    Y[3,i] = SURV3*Y[2, i-1]

for i in range(0,n-1):
    lam[0,i] = Y[0,i+1]/Y[0, i]
    lam[1,i] = Y[1,i+1]/Y[1, i]
    lam[2,i] = Y[2,i+1]/Y[2, i]
    lam[3,i] = Y[3,i+1]/Y[3, i]
    
print("\n Lambda condenses to: ", (lam[1,i]+lam[2,i]+lam[3,i])/3)
print("\n Remember you can view actual population values change by viewing the full matrix 'Y'")
    
    
    
    
    