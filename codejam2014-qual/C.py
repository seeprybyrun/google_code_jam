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
    return f.readline().strip()

def solve(R,C,M):

    if R*C - M in impossible: return 'Impossible'
    
    grid = ['.' * C for _ in range(R)]
    for m in range

infile = sys.argv[1]
f = open(infile,'r')

rows = []
cols = []
mines = []

T = int(next_line(f))
for t in range(T):
    R,C,M = map(float,next_line(f).split())
    rows.append(R)
    cols.append(C)
    mines.append(M)
f.close()

for t,R,C,M in zip(range(T),rows,cols,mines):
    print 'Case #{}: {}'.format(t+1,solve(R,C,M))
