"""
	Work of David Yan, Williams College Class of 2015
	Contact at davidyan93@gmail.com
"""

import math

# brute force solution is elegant and relatively fast
def main():
    squareSum = math.pow((50*101), 2)

    sumSquares = 0

    for i in xrange(1, 101):
        sumSquares += math.pow(i, 2)

    print squareSum - sumSquares

if __name__ == "__main__":
    main()
