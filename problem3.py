"""
	Work of David Yan, Williams College Class of 2015
	Contact at davidyan93@gmail.com
"""

import math

# Naive prime checking approach
def isPrime(num):
	for i in xrange(2, num):
		if num % i == 0:
			return False
	return True

def largestPrimeFactor(goal, largest):
	current = 2

	# Reduce to subproblems as often as possible
	while current < goal:
		if goal % current == 0:
			if isPrime(current):
				if current > largest:
					return largestPrimeFactor((goal / current), current)
				else:
					return largestPrimeFactor((goal / current), largest)
		current += 1

	# if we get to here, no other prime factors, so check if where we are is currently prime.
	if isPrime(goal):
		return goal
	else:
		return largest


def main():
	print largestPrimeFactor(600851475143, 0)

if __name__ == "__main__":
	main()