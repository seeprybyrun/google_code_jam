#!/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import sys
from decimal import *
import itertools as it
from math import sqrt
from math import floor
from math import ceil
from math import log
from math import log10
import time
import random

inf = float('inf')

def next_line(filename):
    return f.readline().strip('\n')

def make_formula(X,Y):
    if len(set(X)) < len(X): return "True"
    f = ''
    T = len(X)
    f = [''] * T
    for t,flavor,malted in zip(range(T),X,Y):
        if malted:
            f[t] += 'not(unmalted[{}])'.format(flavor-1)
        else:
            f[t] += 'unmalted[{}]'.format(flavor-1)
    return ' or '.join(f)

def solve_brute_force(N,M,T,X,Y):
    unmalted = [True] * N
    num_malted = 0
    formulas = [make_formula(X[m],Y[m]) for m in range(M)]
    satisfied = True

    for num_malted in range(N+1):
        for comb in it.combinations(range(N),num_malted):
##            print comb
            unmalted = [not(i in comb) for i in range(N)]
            satisfied = True
            for f in formulas:
                if not eval(f):
##                    print unmalted,f
                    satisfied = False
                    break
            if satisfied:
                break
        if satisfied:
            break

    if satisfied:
        assert set([eval(f) for f in formulas]) == set([True])
        return ' '.join(['0' if unmalted[n] else '1' for n in range(N)])
    else:
        return 'IMPOSSIBLE'

def solve(N,M,T,X,Y):
    unmalted = [True] * N
    num_malted = 0
    formulas = [make_formula(X[m],Y[m]) for m in range(M)]
##    print formulas
    
    satisfied = False
    while not satisfied:
        satisfied = True
        for m,f in enumerate(formulas):
            if not eval(f):
##                print unmalted, 'does not satisfy', f
                satisfied = False
                satisfiable = False
                # find first unmalted flavor the customer wants malted and flip
                for t,flavor,wants_malted in zip(range(T[m]),X[m],Y[m]):
                    if wants_malted and unmalted[flavor-1]:
##                        print 'setting unmalted[{}] = False'.format(flavor-1)
                        satisfiable = True
                        unmalted[flavor-1] = False
                        num_malted += 1
                        break
                if not satisfiable:
##                    print 'unable to satisfy', f
                    return 'IMPOSSIBLE'
                break

    assert set([eval(f) for f in formulas]) == set([True])
    return ' '.join(['0' if unmalted[n] else '1' for n in range(N)])

infile = sys.argv[1]
f = open(infile,'r')

C = int(next_line(f))
N = [None] * C
M = [None] * C
T = [None] * C
X = [None] * C
Y = [None] * C

for c in range(C):
    N[c] = int(next_line(f))
    M[c] = int(next_line(f))
    T[c] = [None] * M[c]
    X[c] = [None] * M[c]
    Y[c] = [None] * M[c]
    for m in range(M[c]):
        this_line_nums = map(int,next_line(f).split())
        T[c][m] = this_line_nums[0]
        X[c][m] = [None] * T[c][m]
        Y[c][m] = [None] * T[c][m]
        for t in range(T[c][m]):
            X[c][m][t] = this_line_nums[2*t+1]
            Y[c][m][t] = (this_line_nums[2*t+2] == 1)
        assert Y[c][m].count(True) <= 1
f.close()

for c in range(C):
    print 'Case #{}: {}'.format(c+1,solve(N[c],M[c],T[c],X[c],Y[c]))
