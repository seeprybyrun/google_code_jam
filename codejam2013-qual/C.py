#!/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import sys
from decimal import *
import itertools as it

def computePreFAS(k):
    preFAS = set([1,2,3])

    def isPalindrome(s):
        return s == s[::-1]

    # definition: a positive integer p is "pre-FAS" if both p and p**2 are
    #   palindromes in base 10; p**2 is called FAS in this case (where FAS
    #   is short for "fair and square")

    # proposition: if p and p**2 are palindromes in base 10 and numDigits(p)
    #   > 1, then p's lead digit is either 1 or 2, p has at most 9 nonzero
    #   digits, and p's nonzero digits are either 1 or 2 (and 2 can only occur
    #   as an end digit or the middle digit of an odd-length p)

    # the code below generates all palindromes in base 10 of this form with
    #   between 2 and k digits (inclusive) and then checks to confirm that
    #   p**2 is a palindrome

    # there are likely other restrictions on palindromes that have 2s as digits,
    #   but this search space is small enough to find all pre-FAS numbers up
    #   to 1e50 in less than a second, which is sufficient to solve the largest
    #   cases in the Google Code Jam problem
    for numDigits in range(1,k/2+1):
        for leadDigit in ['1','2']:
            
            # the number of nonzero digits in the first half of the palindrome
            #   is at most 4 or the number of digits total; we don't go up to
            #   min(4,numDigits) because the lead digit is already nonzero
            for numNonZero in range(min(4,numDigits)):
                
                # this chooses where to put the nonzero digits in the first
                #   half of the palindrome
                for x in it.combinations(range(1,numDigits),numNonZero):
                    y = [leadDigit] + ['0']*(numDigits-1)
                    for index in x:
                        y[index] = '1'
                    s1 = ''.join(y)
                    s2 = s1[::-1]
                    
                    # here we get a palindrome of length 2*numDigits
                    candidates = [int(s1+s2)]
                    
                    # and then, if we're not at k digits already, we generate
                    #    palindromes of odd length (2*numDigits+1)
                    if len(s1) < k/2 or k % 2 == 1:
                        candidates += [int(s1+d+s2) for d in '012']

                    # finally, test all the candidates we generated
                    for p in candidates:
                        if isPalindrome(str(p**2)):
                            preFAS.add(p)

    return preFAS

def solve(preFAS,sqrtA,sqrtB):
    # we check preFAS numbers because they are smaller than the FAS numbers
    # this method actually takes the most time per call: probably can
    #   be more efficient than the list comprehension, but it works for the
    #   GCJ problem (~8 seconds for all calls in the large-2 case)
    return len([p for p in preFAS if sqrtA <= p <= sqrtB])

T = 0 # number of test cases
endpts = []
lowerBd = float('inf')
upperBd = -float('inf')
getcontext().prec = 100

infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof

    if i == 0: # first line tells us T
        T = int(line)
    else: # other lines give A,B
        A,B = map(int,line.split())
        # using the decimal package allows us to get enough precision
        #   in taking the square roots of the big numbers
        sqrtA = int(Decimal(A).sqrt().quantize(Decimal('1.'), rounding=ROUND_UP))
        sqrtB = int(Decimal(B).sqrt().quantize(Decimal('1.'), rounding=ROUND_DOWN))
        endpts.append((sqrtA,sqrtB))
        lowerBd = min(lowerBd,sqrtA)
        upperBd = max(upperBd,sqrtB)
f.close()

# max number of digits in palindromes to consider: effectively
#   ceil(log10(upperBd))
k = int(Decimal(upperBd).log10().quantize(Decimal('1.'), rounding=ROUND_UP))
preFAS = computePreFAS(k)

for i in range(1,T+1):
    A,B = endpts[i-1]
    print 'Case #{}: {}'.format(i,solve(preFAS,A,B))
