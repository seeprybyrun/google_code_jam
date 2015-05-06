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
import re

inf = float('inf')

def next_line(filename):
    return f.readline().strip('\n')

##def solve(language,pattern):
##    return sum([1 if pattern.match(w) else 0 for w in language])

infile = sys.argv[1]
f = open(infile,'r')

L,D,N = map(int,next_line(f).split())
language = [None]*D

for d in range(D):
    language[d] = next_line(f)
for n in range(N):
    signal = next_line(f).replace('(','[').replace(')',']')
    pattern = re.compile(signal)
    matches = sum([1 if pattern.match(w) else 0 for w in language])
    print 'Case #{}: {}'.format(n+1,matches)
f.close()
