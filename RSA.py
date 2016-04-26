# RSA.py
# Author: Jason Duffey
# Date: 03/2016
# An implementation of RSA assymetric encryption
# NOTE: This is not a secure implementation
# Only use for educational purposes
import random

_mrpt_num_trials = 7

def modular_multiplicative_inverse(a, n):
    t = 0
    nt = 1
    r = n
    nr = a % n

    if(n < 0):
        n = -n

    if(a < 0):
        a = n - (-a % n)

    while(nr != 0):
        quot = (r/nr) | 0;
        temp = nt
        nt = t - quot*nt
        t = temp
        temp = nr
        nr = r - quot*nr
        r = temp

    if(r > 1):
        return -1

    if (t < 0):
        t = t + n
    return t

def generatePrime():
    isPrime = 0
    while(not isPrime):
        p = random.randint(4000000, 4000000000)
        isPrime = checkPrime(p)

    if(isPrime):
        return p

def checkPrime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite



def generateKeys():
    p = generatePrime()
    q = generatePrime()
    n = p * q
    t = (p - 1) * (q - 1)

    d = random.randrange(1, t)
    e = modular_multiplicative_inverse(d,t)

    f = open('public.txt', 'w')
    f.write(str(n) + "\n" + str(e))
    f.close()

    f = open('private.txt', 'w')
    f.write(str(n) + "\n" + str(d))
    f.close()

