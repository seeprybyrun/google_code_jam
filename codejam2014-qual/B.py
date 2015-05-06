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

def solve(C,F,X):
    # by calculus, the min will occur around k ~ X/C - 2/F
    k0 = X/C - 2./F

    if k0 <= 0:
        lower = 0
        upper = 10
    else:
        lower = int(floor(0.9*k0))
        upper = int(ceil(1.1*k0))+1
    
    time_to_kth_farm = {0: 0}
    for k in range(1,upper):
        time_to_kth_farm[k] = time_to_kth_farm[k-1] + C/(2.+(k-1)*F)

    times_to_goal = [time_to_kth_farm[k]+X/(2.+k*F) for k in range(lower,upper)]
    return min(times_to_goal)

infile = sys.argv[1]
f = open(infile,'r')

farm_price = []
farm_output = []
goal = []

T = int(next_line(f))

for t in range(T):
    C,F,X = map(float,next_line(f).split())
    farm_price.append(C)
    farm_output.append(F)
    goal.append(X)
f.close()

for t,C,F,X in zip(range(T),farm_price,farm_output,goal):
    print 'Case #{}: {}'.format(t+1,solve(C,F,X))
