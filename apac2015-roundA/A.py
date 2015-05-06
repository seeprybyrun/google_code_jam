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

def numeralRepr(s):
    assert len(s) == 7
    for d in s:
        assert d in '01'
    outstr = [['.','.','.','.','.'],
              ['.',' ',' ',' ','.'],
              ['.','.','.','.','.'],
              ['.',' ',' ',' ','.'],
              ['.','.','.','.','.']]
    if s[0] == '1':
        outstr[0][1] = '#'
        outstr[0][2] = '#'
        outstr[0][3] = '#'
    if s[1] == '1':
        outstr[0][4] = '#'
        outstr[1][4] = '#'
        outstr[2][4] = '#'
    if s[2] == '1':
        outstr[2][4] = '#'
        outstr[3][4] = '#'
        outstr[4][4] = '#'
    if s[3] == '1':
        outstr[4][3] = '#'
        outstr[4][2] = '#'
        outstr[4][1] = '#'
    if s[4] == '1':
        outstr[4][0] = '#'
        outstr[3][0] = '#'
        outstr[2][0] = '#'
    if s[5] == '1':
        outstr[2][0] = '#'
        outstr[1][0] = '#'
        outstr[0][0] = '#'
    if s[6] == '1':
        outstr[2][1] = '#'
        outstr[2][2] = '#'
        outstr[2][3] = '#'
    return '\n'.join([''.join(row) for row in outstr])

def possibleNumerals(s,union):
    assert len(s) == 7
    for d in s:
        assert d in '01'

    possible = set(range(10))
    if s[0] == '1':
        possible &= set([0,2,3,5,6,7,8,9])
    elif union[0] == '1':
        possible &= set([1,4])
        
    if s[1] == '1':
        possible &= set([0,1,2,3,4,7,8,9])
    elif union[1] == '1':
        possible &= set([5,6])
        
    if s[2] == '1':
        possible &= set([0,1,3,4,5,6,7,8,9])
    elif union[2] == '1':
        possible &= set([2])
        
    if s[3] == '1':
        possible &= set([0,2,3,5,6,8,9])
    elif union[3] == '1':
        possible &= set([1,4,7])
        
    if s[4] == '1':
        possible &= set([0,2,6,8])
    elif union[4] == '1':
        possible &= set([1,3,4,5,7,9])
        
    if s[5] == '1':
        possible &= set([0,4,5,6,8,9])
    elif union[5] == '1':
        possible &= set([1,2,3,7])
        
    if s[6] == '1':
        possible &= set([2,3,4,5,6,8,9])
    elif union[6] == '1':
        possible &= set([0,1,7])

    return possible

def intersectStr(s,t):
    assert len(s) == len(t)
    ret = ''
    for c,d in zip(s,t):
        assert c in ['0','1','?']
        assert d in ['0','1','?']
        if c == '0' or d == '0':
            ret += '0'
        elif c == '?' or d == '?':
            ret += '?'
        else:
            ret += '1'
    assert len(ret) == len(s) == len(t)
    return ret

def negateStr(s):
    for c in s:
        assert c in ['0','1']
        if c == '0':
            ret += '1'
        else:
            ret += '0'
    assert len(ret) == len(s)
    return ret

fullState = { 0: '1111110',
              1: '0110000',
              2: '1101101',
              3: '1111001',
              4: '0110011',
              5: '1011011',
              6: '1011111',
              7: '1110000',
              8: '1111111',
              9: '1111011'}

def stateRepr(n,mask='1111111'):
    assert 0 <= n <= 9
    return intersectStr(fullState[n],mask)

def solve(states):
    union = ['0']*7
    for s in states:
        for i in range(7):
            if s[i] == '1':
                union[i] = '1'
    union = ''.join(union)
    possibleNums = [possibleNumerals(s,union) for s in states]
    possibleAnswerNums = []
    possibleStartNums = []
    for startNum in range(10):
        thisNum = startNum
        isGood = True
        for pn in possibleNums:
            if thisNum not in pn:
                isGood = False
                break
            thisNum -= 1
            thisNum %= 10
        if isGood:
            possibleAnswerNums.append(thisNum)
            possibleStartNums.append(startNum)
    if not possibleAnswerNums:
        return 'ERROR!' # no possible answer found'
    else:
        maskedAnswers = set()
        for answerNum,startNum in zip(possibleAnswerNums,possibleStartNums):
            mask = computeMask(states,startNum)
            maskedAnswers.add(stateRepr(answerNum,mask))
        if len(maskedAnswers) > 1:
            return 'ERROR!' # more than one possible answer: {}'.format(maskedAnswers)
        else:
            ret = list(maskedAnswers)[0]
            if '?' in ret:
                return 'ERROR!' # unable to determine if a light is on: {}'.format(ret)
            return ret

def computeMask(states,startNum):
    mask = ['?'] * 7
    n = startNum
    for s in states[:10]: # need at most 10 states
        fs = fullState[n]
        for i in range(7):
            assert not(fs[i] == '0' and s[i] == '1')
            if fs[i] == '1' and s[i] == '0':
                mask[i] = '0'
            elif fs[i] == '1' and s[i] == '1':
                mask[i] = '1'
            # no info gained if fs[i] == s[i] == '0'
        n -= 1
        n %= 10
    return ''.join(mask)

T = 0 # number of test cases

##print numeralRepr('0011111')
##print numeralRepr('0011011')

infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof

    if i == 0: # first line tells us T
        T = int(line)
    else: # other lines give the states
        states = line.split()[1:] # first item in split is number of states
        print 'Case #{}: {}'.format(i,solve(states))
f.close()
