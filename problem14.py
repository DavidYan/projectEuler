"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com
"""

# We're going to be using a dynamic programming-like approach, where we memo-ize previously done work so we don't have to it again. Once again, the raw power of computers allows us to escape difficult workarounds.

# We'll calculate the chain size by recursion.
def collatzSize(num, memos):
    # Base case
    if num == 1:
        return 1

    # Check if we've already calculated this number before.
    if num < len(memos) and memos[num] > 0:
        return memos[num]

    # Otherwise, do raw calculation. Luckily Python is pass by assignment (aka pass by reference) so I'm not too worried about passing arbitrarily large lists. 
    if num % 2 == 0:
        size = 1 + collatzSize((num/2), memos)
    else:
        size = 1 + collatzSize((3*num) + 1, memos)

    # Memorize our calculation so we don't have to do this again.
    if num < len(memos):
        memos[num] = size
    
    return size

def main():
    memoList = []

    # List size randomly chosen.
    for i in xrange(3000000):
        memoList.append(0)

    max = 0
    actualNumber = 0
    for j in xrange(1, 1000000):
        chainSize = collatzSize(j, memoList)
        if chainSize > max:
            max = chainSize
            actualNumber = j

    print actualNumber

if __name__ == "__main__":
    main()
