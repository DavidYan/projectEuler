"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

# naive approach
def isPrime(num):
    current = 2

    while current < num:
        if num%current==0:
            return False
        current += 1

    return True

# brute force, baby
def nthPrime(target):
    current = 2
    num = 0
    while True:
        if isPrime(current):
            num += 1
            if num == target:
                return current
        current += 1

def main():
    print nthPrime(10001)

if __name__ == '__main__':
    main()
