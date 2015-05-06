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

press_for = { 'a' : 2, 'b' : 2, 'c' : 2,
              'd' : 3, 'e' : 3, 'f' : 3,
              'g' : 4, 'h' : 4, 'i' : 4,
              'j' : 5, 'k' : 5, 'l' : 5,
              'm' : 6, 'n' : 6, 'o' : 6,
              'p' : 7, 'q' : 7, 'r' : 7, 's' : 7,
              't' : 8, 'u' : 8, 'v' : 8,
              'w' : 9, 'x' : 9, 'y' : 9, 'z' : 9,
              ' ' : 0 }
letters_corresponding_to = [ ' ',  None,  'abc', 'def',
                             'ghi', 'jkl', 'mno', 'pqrs',
                             'tuv', 'wxyz' ]

def solve(s):
    output = ''
    prev_digit = -1
    for c in s:
        d = press_for[c]
        if d == prev_digit:
            output += ' '
        i = letters_corresponding_to[d].find(c)
        output += str(d) * (i+1)
        prev_digit = d
    return output

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
