"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com    
"""

# This problem is only easy due to the fact that computation power has risen so high and programming languages being able to handle 64bit numbers now. 

# As a future challenge, I might consider how I would do this problem knowing I only had access to 32bit unsigned ints.
def readNums():
    sum = 0
    with open('problem13Nums.txt') as gridFile:
        for i in gridFile.readlines():
            sum += int(i)
    return sum

def main():
    print str(readNums())[:10]

if __name__ == "__main__":
    main()
