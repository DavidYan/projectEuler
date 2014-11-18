"""
	Work of David Yan, Williams College Class of 2015
	Contact at davidyan93@gmail.com
"""

import math

# Thanks to the power of current computing, this brute-forceable
# Problem also tells us there's only 1 configuration

def checkPyth(a, b, c):
	return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

def main():
	# iterate through all possible combinations of a, b, and c
	# Don't have to worry about case where a, b, or c is equal to 0
	for a in xrange(1, 1000):
		for b in xrange(1, 1000):
			for c in xrange(1, 1000):
				if (a+b+c) == 1000 and checkPyth(a, b, c):
					print a*b*c
					return

if __name__ == "__main__":
	main()