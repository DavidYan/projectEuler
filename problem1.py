"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

def main():
    sum = 0

    for i in xrange(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print sum

if __name__ == "__main__":
    main()
