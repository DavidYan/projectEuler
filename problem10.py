"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

import math

# Looks like fast prime checking might be indispensable in the future
# Currently going to use Sieve of Eratosthenes, might want to upgrade in the future
def getPrimes(num):
    primes = []
    sieve = []

    # initialize sieve
    for i in xrange(num+1):
        sieve.append(True)

    # Actually do the sieving
    for j in xrange(2, num+1):
        if sieve[j]:
            primes.append(j)

            # Sieve does actual work here. For loops are perfect for this
            for k in xrange(j*j, num+1, j):
                sieve[k] = False

    return primes

def main():

    sum = 0
    primes = getPrimes(2000000)

    for i in primes:
        sum += i

    print sum

if __name__ == "__main__":
    main()
