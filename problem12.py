"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

import math

def check500Divisors(num):
    amt = 0
    current = 1
    end = int(math.sqrt(num))

    # Check if num is a perfect square
    if math.pow(end, 2) == num:
        amt += 1

    while current < end:
        if num%current == 0:
            # Otherwise we get 2 free divisors while only needing to search for 1
            amt += 2
            if amt >= 500:
                return True
        
        current += 1

    return False

def getTriNumber(seed):
    return (seed*(seed+1)) / 2

def main():
    current = 8
    while True:
        triNumber = getTriNumber(current)
        if check500Divisors(triNumber):
            print triNumber
            return

        current += 1

if __name__ == "__main__":
    main()
