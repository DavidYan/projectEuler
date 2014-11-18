"""
	Work of David Yan, Williams College Class of 2015
	Contact at davidyan93@gmail.com
"""

import math

def checkPalindrome(num):
	numString = str(num)
	return numString==numString[::-1] # List comprehensions are a wonderful thing

def main():
	largest = 0
	for i in xrange(1000):
		for j in xrange(1000):
			product = i*j
			if checkPalindrome(product) and product > largest:
				largest = product

	print largest

if __name__ == "__main__":
	main()