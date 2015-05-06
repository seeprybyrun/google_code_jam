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

def solve(s):
    return ' '.join(s.split()[::-1])

infile = sys.argv[1]
f = open(infile,'r')

T = int(next_line(f))
S = [None] * T

for t in range(T):
    s = next_line(f)
    S[t] = s
f.close()

for t,s in zip(range(T),S):
    print 'Case #{}: {}'.format(t+1,solve(s))
