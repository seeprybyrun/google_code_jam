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

MANY_CARDS = "Bad magician!"
NO_CARDS = "Volunteer cheated!"

def solve(r1,arrangement1,r2,arrangement2):
    #print r1,arrangement1
    #print r2,arrangement2
    answers = set(arrangement1[r1-1]) & set(arrangement2[r2-1])
    #print answers
    if len(answers) == 1:
        return list(answers)[0]
    elif len(answers) == 0:
        return NO_CARDS
    else:
        return MANY_CARDS

infile = sys.argv[1]
f = open(infile,'r')

answer1 = []
arrangement1 = []
answer2 = []
arrangement2 = []

T = int(next_line(f))

for t in range(T):
    answer1.append(int(next_line(f)))
    cards1 = []
    for i in range(4):
        cards1.append(map(int,next_line(f).split()))
    arrangement1.append(cards1)
    answer2.append(int(next_line(f)))
    cards2 = []
    for i in range(4):
        cards2.append(map(int,next_line(f).split()))
    arrangement2.append(cards2)
f.close()

for t in range(T):
    print 'Case #{}: {}'.format(t+1,solve(answer1[t],arrangement1[t],answer2[t],arrangement2[t]))
