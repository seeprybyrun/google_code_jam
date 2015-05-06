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

def solve():
    
    return '{}'.format()

num_lines = 2 # number of lines per test case
infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof

    if i == 0: # first line tells us # of test cases
        pass
    elif i%num_lines == 1:
        pass
    elif i%num_lines == 0:
        M = map(int,line.split())
        print 'Case #{}: {}'.format(i/N,solve(M))
f.close()
