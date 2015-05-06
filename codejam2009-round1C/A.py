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
import string

inf = float('inf')

def next_line(filename):
    return f.readline().strip('\n')

def solve(s):
    mapping = {c: -1 for c in alphabet}
    digit = 1
    base = 0
    for c in s:
        if mapping[c] < 0:
            base += 1
            mapping[c] = digit
            if digit == 1:
                digit = 0
            elif digit == 0:
                digit = 2
            else:
                digit += 1
    tot = 0
    base = max(base,2)
    for i,c in enumerate(s[::-1]):
        tot += mapping[c] * (base ** i)
    return tot

infile = sys.argv[1]
f = open(infile,'r')

T = int(next_line(f))
alphabet = string.ascii_lowercase + string.digits
for t in range(T):
    countdown = next_line(f)
    print 'Case #{}: {}'.format(t+1,solve(countdown))
f.close()
