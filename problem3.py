import math
import random
from decimal import Decimal

# Naive prime checking approach
def isPrime(num):
	prime = True
	for i in xrange(2, num):
		if num%i == 0:
			prime = True
			break # Don't need to check further
	return prime

#overflow issues.

#okay divide locally
def largestPrimeFactor(num):
	current = 0
	for i in xrange(2, num):
		if isPrime(i) and num%i == 0: # I hope python is a lazy evaluator....
			current = i
			return largestPrimeFactor(num / i) # Attempt to recursively make this smaller

	return current

def main():
	print largestPrimeFactor(Decimal(600851475143))

if __name__ == "__main__":
	main()