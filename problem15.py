"""
   Work by David Yan, Williams College Class of 2015
   Contact at davidyan93@gmail.com
"""

def initProblem(num):
    mainGrid = []
    # We want to memorize values to prevent trying to solve the same subproblem over and over again
    # Recall that our grid represents each corner position, so we need to offset by 1
    for i in xrange(num+1):
        row = []
        for j in xrange(num+1):
            # Last row and last column only have 1 path to endpoint
            if j == (num) or i == (num):
                row.append(1)
            else:
                row.append(0) # Otherwise initialize all values to be empty
        mainGrid.append(row)

    return gridPaths(0, 0, mainGrid)


# Recursion and memoization makes this problem easy.
def gridPaths(posX, posY, grid):
    offsetX = grid[posX+1][posY]
    offsetY = grid[posX][posY+1]

    if offsetX > 0 and offsetY > 0: # Means we've seen both entries before
        numPaths = offsetX + offsetY
    elif offsetX > 0: # Only one path seen
        numPaths = offsetX + gridPaths(posX, posY+1, grid)
    elif offsetY > 0: # Do as little work as possible
        numPaths = offsetX + gridPaths(posX+1, posY, grid)
    else: # Worst case, no known data, continue exploring
        numPaths = gridPaths(posX+1, posY, grid) + gridPaths(posX, posY+1, grid)

    # Update our grid, and return the value
    grid[posX][posY] = numPaths    
    return numPaths


def main():
    print initProblem(20)

if __name__ == "__main__":
    main()
