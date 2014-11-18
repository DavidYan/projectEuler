"""
	Work of David Yan, Williams College Class of 2015
	Contact at davidyan93@gmail.com
"""

import math

# Looks a lot like problem 2 in the Green Chicken, so we'll use that approach

def checkContribution(num, factors):
	for i in xrange(2, len(factors)):
		# check case where number has prime factors but isn't a power
		power = float(math.log(num, i))
		if num%i==0 and not power.is_integer():
			return
		# now all numbers we catch from the log function must be powers of primes
		elif power.is_integer():
			factors[i] = num
			return

def main():
	current = 1

	# This will eventually represent the highest number that is a power of that index.
	# Will eventually iterate through all the values, multiplying them all together.
	contributingFactors = []

	for i in xrange(20):
		contributingFactors.append(1) # initialize as all 1s

	for i in xrange(2, 21):
		checkContribution(i, contributingFactors) # process the numbers 2 through 20

	for i in xrange(len(contributingFactors)):
		current *= contributingFactors[i] # find the Least Common Multiple
	print current

if __name__ == "__main__":
	main()