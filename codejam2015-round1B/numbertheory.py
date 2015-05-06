from math import sqrt,floor,ceil,log,log10,exp
from operator import mul
import itertools as it

primesMemo = {}
divisorsMemo = {}
sumOfDivisorsMemo = {}

def prod(iterable):
    return reduce(mul, iterable, 1)

def divisors(n):
    # trial division
    if n not in divisorsMemo:
        upperBound = int(floor(sqrt(n)))+1
        divs = [i for i in range(1,upperBound) if n % i == 0]
        divs.extend([n/i for i in divs if i*i != n])
        divs = []
##        for i in range(1,upperBound):
##            if n % i == 0:
##                divs.append(i)
##                if n/i != i:
##                    divs.append(n/i)
        divisorsMemo[n] = divs
    return divisorsMemo[n]

def sumOfDivisors(n):
    if n not in sumOfDivisorsMemo:
        sumOfDivisorsMemo[n] = sum(divisors(n))
    return sumOfDivisorsMemo[n]

def sumOfProperDivisors(n):
    return sumOfDivisors(n) - n

def areAmicable(a,b):
    return (a != b) and (a == sumOfProperDivisors(b)) and (b == sumOfProperDivisors(a))

def allAmicableNumbersLessThan(n):
    amicableNums = []
    for i in range(1,n):
        j = sumOfProperDivisors(i)
        if areAmicable(i,j):
            amicableNums.append(i)
    return amicableNums

def isPrimeNoSieve(n):
    rootN = int(floor(sqrt(n)))
    if primesMemo['maxPrime'] <= rootN:
        raise Exception
    for p in allPrimesUpTo(rootN+1):
        if n % p == 0:
            return False
    return True

def eratoSieve(m):
    n = int(floor(m))
    print 'computing sieve of Eratosthenes up through {}'.format(n)
    prime = [True]*(n+1)
    sqrtN = int(floor(sqrt(n)))
    
    for d in range(2,sqrtN+1):
        if prime[d]:
            for j in range(d**2,n+1,d):
                prime[j] = False
    primesMemo['maxPrime'] = n
    primesMemo['isPrime'] = prime

def allPrimesUpTo(m):
    n = int(floor(m))
    
    if 'maxPrime' not in primesMemo or primesMemo['maxPrime'] <= n:
        eratoSieve(n)
        
    if 'primes' in primesMemo:
        return [p for p in primesMemo['primes'] if p < n]
        
    primes = []
    for i in range(2,n):
        if isPrime(i):
            primes.append(i)
            
    primesMemo['primes'] = primes
    return primes

def isPrime(n):
    if n <= 1:
        return False
    
    if 'maxPrime' in primesMemo and primesMemo['maxPrime'] > n:
        return primesMemo['isPrime'][n]
    
    bits = int(floor(log(n)/log(2)) + 1)
    eratoSieve(2**bits)
    return primesMemo['isPrime'][n]

##eratoSieve(100)
##for i in range(100):
##    if isPrime(i):
##        print '{0} is prime'.format(i)

def euclidExtended(x,y):
    """Returns (a,b) such that a*x + b*y == 1. Returns None if no such integers exist."""
    # special cases
    if x**2 == 1: # if x == +- 1
        return (x,0)
    if y**2 == 1: # if y == +- 1
        return (0,y)
    if x*y == 0 or x%y == 0 or y%x == 0: # if x|y or y|x
        return None
    
    switched = False
    fail = False
    
    if abs(x) > abs(y):
        x,y = y,x
        switched = True
        
    a = [1,0]
    b = [0,1]
    
    while True:
        q = x/y
        r = x%y
        a.append(a[-2]-q*a[-1])
        b.append(b[-2]-q*b[-1])
        x,y = y,r
        if r == 1:
            break
        if r == 0:
            return None

    if switched:
        return b[-1],a[-1]
    return a[-1],b[-1]

##print euclidExtended(1,1)
##print euclidExtended(2,3)
##print euclidExtended(5,3)
##print euclidExtended(2,4)
##print euclidExtended(0,1)
##print euclidExtended(1,0)
##print euclidExtended(4,6)
##print euclidExtended(-2,3)
##print euclidExtended(10,3)
##print euclidExtended(3,10)

def crt(r,m):
    """Given a list of integers r and a list of positive coprime integers m, 
returns the integer 0 <= x < N, where N is the product of the elements of m, such
that x is congruent to r[i] modulo m[i]."""
    N = reduce(mul, m, 1) #product of elements of m

    # use extended euclidean algorithm to find a,b such that a*m_i + b*m_j == 1
    # so a*m_i == 1 mod m_j, so a*m_i*r_j == r_j mod m_j
    # and b*m_j == 1 mod m_i, so b*m_j*r_i == r_i mod m_i
    # so we can take x == a*m_i*r_j + b*m_j*r_i (mod m_i*m_j)
    # then take r_i = x, m_i = m_i*m_j, and set r_j and m_j to the next ones in the list, and repeat

    r_i,m_i = r[0],m[0]
    r_i %= m_i
    
    n = len(zip(r,m))
    for j in range(1,n):
        r_j,m_j = r[j],m[j]
        a,b = euclidExtended(m_i,m_j)
        r_i = a*m_i*r_j + b*m_j*r_i
        m_i = m_i*m_j
        r_i %= m_i

    return r_i

#print crt([1,4,1],[2,17,9])

def powmod(a,b,m):
    # TODO: is this faster using the Euler totient function to reduce the exponent?
    prod = 1
    for i in range(b):
        prod *= a
        prod %= m
    return prod

def totient(primeDivisors,n=None):
    """Takes a list of the form [k_2,k_3,k_5,...] that gives
the number of powers of the ith prime dividing a number, and
outputs the totient of the number."""

    primes = []
    if n:
        primes = allPrimesUpTo(n)
    else:
        primes = primesMemo['primes']

    totient = 1
    for i,k in enumerate(primeDivisors):
        if k == 0: continue
        p = primes[i]
        totient *= p**k - p**(k-1)
    return totient

def primeFactorGenerator(M):
    '''Generates all lists P of tuples (p,k) of primes p and integers k such
that 1 <= prod([p**k for p,k in P]) < M. Note: Requires M >= 81.'''
    primes = allPrimesUpTo(M-1)
    
    root5N = int(floor(M**(0.2)))
    root4N = int(floor(M**(0.25)))
    cbrtN = int(floor(M**(1./3)))
    sqrtN = int(floor(sqrt(M)))
    tinyPrimes = [p for p in primes if p <= root5N]
    logByTinyPrimes = [log(M)/log(p) for p in tinyPrimes]
    verySmallPrimes = [p for p in primes if root5N < p <= root4N] # at most 4
    minVerySmall = verySmallPrimes[0]
    smallPrimes = [p for p in primes if root4N < p <= cbrtN] # at most 3
    mediumPrimes = [p for p in primes if cbrtN < p <= sqrtN] # at most 2
    largePrimes = [p for p in primes if sqrtN < p <= M/minVerySmall] # at most 1
    veryLargePrimes = [p for p in primes if M/minVerySmall < p <= M/2] # can only be paired with tiny primes
    superMassivePrimes = [p for p in primes if p > M/2] # only possible prime

    bigFactorsList = []
    for i in [0,1]:
        for x in it.combinations_with_replacement(largePrimes,i):
            lp = [p for p in x]
            for j in range(2-i+1):
                for y in it.combinations_with_replacement(mediumPrimes,j):
                    mp = [p for p in y]
                    if prod(lp + mp) >= M: continue
                    for k in range(3-i-j+1):
                        for z in it.combinations_with_replacement(smallPrimes,k):
                            sp = [p for p in z]
                            if prod(lp + mp + sp) >= M: continue
                            for m in range(4-i-j-k+1):
                                for w in it.combinations_with_replacement(verySmallPrimes,m):
                                    vsp = [p for p in w]
                                    bf = lp + mp + sp + vsp
                                    if prod(bf) >= M: continue
                                    bigFactorsList.append(bf)
    for p in veryLargePrimes:
        bigFactorsList.append([p])

    for bf in bigFactorsList:
        bigPrimes = sorted(set(bf))
        bigPowers = [bf.count(p) for p in bigPrimes]
        tinyPowers = [0 for p in tinyPrimes]
        while tinyPowers[-1] >= 0:
            primeList = [p for i,p in enumerate(tinyPrimes) if tinyPowers[i] > 0] + bigPrimes
            powerList = [k for k in tinyPowers if k > 0] + bigPowers
            primesAndPowers = zip(primeList,powerList)
            # compute sum of divisors for current set of factors and record sum of proper divisors               
            n = prod([p**k for p,k in zip(primeList,powerList)])
            if n < M:
                yield primesAndPowers
                tinyPowers[0] += 1
                mostRecentlyChanged = 0
            if n >= M:
                if mostRecentlyChanged == len(tinyPowers)-1:
                    tinyPowers[-1] = -1
                    break
                for i in range(mostRecentlyChanged+1):
                    tinyPowers[i] = 0
                tinyPowers[mostRecentlyChanged+1] += 1
                mostRecentlyChanged += 1

            # update prime factorization
            # check for carry
            for i in range(mostRecentlyChanged,len(tinyPowers)):
                if tinyPowers[i] >= logByTinyPrimes[i]:
                    if i < len(tinyPowers)-1:
                        tinyPowers[i] = 0
                        tinyPowers[i+1] += 1
                        mostRecentlyChanged = i+1
                    else:
                        # end the phase
                        tinyPowers[-1] = -1
                        break
                else:
                    break

    for p in superMassivePrimes:
        yield [(p,1)]

##M = 81
##L = [prod([p**k for p,k in P]) for P in primeFactorGenerator(M)]
##assert sorted(L) == range(1,M)
