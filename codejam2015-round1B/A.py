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

def solve(n):
    num_digits = int(floor(log10(n))) + 1
    # amount to get from 1 to 10^k is sum_{i=0}^k (10 + sum_{j=1}^i 9 * 10^j)
    if n <= 10:
        return n
    if n <= 99:
        return 10 + sum(map(int,str(n)))
    if n == 100:
        return 10 + (10 + 9)
    if n <= 999:
        s = str(n)
        return 10 + (10 + 9) + int(s[0]) + int(s[1:])

print solve(999)

nums = []
infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof
    if i == 0: # first line tells us # of test cases
        pass
    else:
        nums.append(int(line))
f.close()
nbrs = compute_neighbors(2*max(nums))
dist = dijkstra(range(2*max(nums)),nbrs,0)[0]

for i in range(len(nums)):
    print 'Case #{}: {}'.format(i+1, dist[nums[i]])
