#!/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import sys
import time

def solve(C,I,L,whichCase):
    for i in range(I):
        for j in range(i+1,I):
            if L[i] + L[j] == C:
                return 'Case #{0}: {1} {2}'.format(whichCase,i+1,j+1)

N = 0 # number of test cases
C = 0 # credit
I = 0 # number of items
L = [] # list of items at store
whichCase = 0

# read input
infile = sys.argv[1] #input("Enter the file name: ")
f = open(infile,'r')

t0 = time.clock()

for i,line in enumerate(f.readlines()):
#    print i,line
    line = line.strip()
    if not line:
        break
    
    # first line tells us N
    if i == 0:
        N = int(line)
    # first line of each test case tells us C
    elif i % 3 == 1:
        C = int(line)
    # second line of each test case tells us I
    elif i % 3 == 2:
        I = int(line)
    # third line of each test case tells us L
    elif i % 3 == 0:
        L = map(int,line.split())
        whichCase += 1
        print solve(C,I,L,whichCase)

t1 = time.clock()
f.close()
#print "seconds elapsed: {0}".format(t1-t0)
