#!/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import sys
#import time
#import copy
#import random
import math
from decimal import *
import itertools as it

getcontext().prec = 100

##def joinIntervals(intervals,A,B):
##    modified = False
##    for (a,b) in copy.copy(intervals):
##        if a <= A and B <= b:
##            try:
##                intervals.remove((A,B))
##            except KeyError:
##                pass
##            return intervals
##        elif a <= A and A <= b and b <= B:
##            intervals.remove((a,b))
##            intervals.add((a,B))
##            A = a
##            modified = True
##        elif A <= a and a <= B and B <= b:
##            intervals.remove((a,b))
##            intervals.add((A,b))
##            B = b
##            modified = True
##        elif A < a and b < B:
##            intervals.remove((a,b))
##            intervals.add((A,B))
##            modified = True
##        else:
##            pass
##    if not modified:
##        intervals.add((A,B))
##    return intervals

def isPalindrome(s):
    #if s[0] != reversed(s).next(): return False
    return s == s[::-1]

##def incrementTernary(n):
##    s = str(n)
##    if set(s) == set(['2']): return int('1' + ('0'*len(s)))
##    
##    digits = [int(c) for c in s]
##    digits[-1] += 1
##    for i in range(len(digits)-1,-1,-1):
##        if digits[i] > 2:
##            digits[i] = 0
##            digits[i-1] += 1
##        else:
##            break
##    return int(''.join(map(str,digits)))
##
##assert incrementTernary(0) == 1
##assert incrementTernary(22) == 100
##assert incrementTernary(1222) == 2000
##assert incrementTernary(101) == 102

##def computeFAS(k): # generate palindromes up to 10**k
##    FAS = set([1,2,3])
##    n = 1
##    while n < 10**(k/2):
##        s1 = str(n)
##        s2 = s1[::-1]
##        # generate palindromes for even-digit numbers
##        candidates = [int(s1+s2)]
##        # then for odd-digit numbers if we're not at k digits already
##        if len(s1) < k or k % 2 == 1:
##            candidates += [int(s1+d+s2) for d in '012']
##        for p in candidates:
##            if isPalindrome(str(p**2)):
##                FAS.add(p)
##                print p
##    return FAS

def computeFAS(k):
    FAS = set([1,2,3])
    for numDigits in range(1,k/2+1):
        for leadDigit in ['1','2']:
            for nonZero in range(min(3,numDigits-1)+1):
                for x in it.combinations(range(1,numDigits),nonZero):
                    y = [leadDigit] + ['0']*(numDigits-1)
                    for index in x:
                        y[index] = '1'
                    s1 = ''.join(y)
                    #print 's1={}'.format(s1)
                    s2 = s1[::-1]
                    # generate palindromes for even-digit numbers
                    candidates = [int(s1+s2)]
                    # then for odd-digit numbers if we're not at k digits already
                    if len(s1) < k or k % 2 == 1:
                        candidates += [int(s1+d+s2) for d in '012']
                    for p in candidates:
                        if isPalindrome(str(p**2)):
                            FAS.add(p)
                            #print p
    return FAS

def solve(FAS,A,B):
    return len( [x for x in FAS if A <= x <= B] )

T = 0 # number of test cases - can ignore this
A = 0 # beginning of interval to search
B = 0 # end of interval to search

infile = ''
customTestCase = False
# if customTestCase active, use that to create the file to be read
if customTestCase:
    f = open('temp','w')
    f.write('''3
1 4
10 120
100 1000
''')
    f.close()
    infile = 'temp'

# otherwise, read input from a file given in the args
else:
    infile = sys.argv[1] #input("Enter the file name: ")

##totalTime = 0

f = open(infile,'r')
endpts = []
lowerBd = float('inf')
upperBd = -float('inf')
for i,line in enumerate(f.readlines()):
#    print i,line
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof
    # first line tells us T
    if i == 0:
        T = int(line)
    else:
##        t0 = time.clock()
        A,B = map(int,line.split())
        sqrtA = int(Decimal(A).sqrt().quantize(Decimal('1.'), rounding=ROUND_UP))
        sqrtB = int(Decimal(B).sqrt().quantize(Decimal('1.'), rounding=ROUND_DOWN))
        endpts.append((sqrtA,sqrtB))
        lowerBd = min(lowerBd,sqrtA)
        upperBd = max(upperBd,sqrtB)
        #print endpts
        #intervals = joinIntervals(intervals,A,B)
        #print intervals
f.close()

#print intervals
# compute all FAS numbers within the intervals we care about
k = int(Decimal(upperBd).log10())
#print maxB,k
FAS = computeFAS(k)
#print FAS,len(FAS)

for i in range(1,T+1):
    A,B = endpts[i-1]
    print 'Case #{}: {}'.format(i,solve(FAS,A,B))

#print "seconds elapsed: {0}".format(t1-t0)
