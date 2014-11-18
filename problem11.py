"""
    Work of David Yan, Williams College Class of 2015
    Contact at davidyan93@gmail.com    
"""

import math

# Too lazy to write in grid by hand, just wrote a txt file with the grid and parsed it.

def readGrid():
    with open('problem11Grid.txt') as gridFile:
        data = [map(int, i.split()) for i in gridFile.readlines()] # List comprehensions are cool

    return data

# Helper methods. Thanks to exception handling we don't have to worry about array bounds
def prodHorizontal(grid, x, y):
    current = grid[x][y]
    try:
        for i in xrange(1, 4):
            current *= grid[x][y+i]
    except IndexError:
        current = 0
    return current
    

def prodDiagonal1(grid, x, y):
    current = grid[x][y]
    try:
        for i in xrange(1, 4):
            current *= grid[x+i][y+i]
    except IndexError:
        current = 0
    return current

def prodDiagonal2(grid, x, y):
    current = grid[x][y]
    try:
        for i in xrange(1, 4):
            current *= grid[x-i][y+i]
    except IndexError:
        current = 0
    return current

def prodVertical(grid, x, y):
    current = grid[x][y]
    try:
        for i in xrange(1, 4):
            current *= grid[x+i][y]
    except IndexError:
        current = 0
    return current

# Iterate through all possible configurations
def main():
    grid = readGrid()
    max = 0

    for i in xrange(len(grid[0])):
        for j in xrange(len(grid)):
            # Only 4 unique shapes. We can reduce checks to associativity of multiplication
            h = prodHorizontal(grid, i, j)
            d1 = prodDiagonal1(grid, i, j)
            d2 = prodDiagonal2(grid, i, j)
            v = prodVertical(grid, i, j)

            if h > max:
                max = h

            if d1 > max:
                max = d1

            if d2> max:
                max = d2

            if v > max:
                max = v

    print max

if __name__ == "__main__":
    main()
