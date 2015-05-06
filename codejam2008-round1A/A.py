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

def dot(v1,v2):
    return sum([a*b for a,b in zip(v1,v2)])

def bruteForceSolve(v1,v2):
    '''no good for len(v1),len(v2) > 6'''
    minDot = float('inf')
    for x in it.permutations(v1):
        for y in it.permutations(v2):
            minDot = min(minDot,dot(x,y))
    return minDot

def solve(v1,v2):
    v1.sort()
    v2.sort(reverse=True)
    return dot(v1,v2)

##f = open('temp','w')
##f.write('blah\n')
##for i in range(1,8):
##    f.write('blah\n')
##    f.write(' '.join(map(str,[random.randint(-1000,1000) for x in range(i)]))+'\n')
##    f.write(' '.join(map(str,[random.randint(-1000,1000) for x in range(i)]))+'\n')
##f.close()

v1 = []
v2 = []

infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof

    if i == 0: # first line tells us # of test cases
        pass
    elif i%3 == 1: # tells us dim of vectors
        pass
    elif i%3 == 2: # other lines give the vectors
        v1 = map(int,line.split())
    elif i%3 == 0:
        v2 = map(int,line.split())
        print 'Case #{}: {}'.format(i/3,solve(v1,v2))
f.close()
