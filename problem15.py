"""
   Work by David Yan, Williams College Class of 2015
   Contact at davidyan93@gmail.com
"""

# Recursion makes this problem hilariously easy.
def gridPaths(posX, posY, gridSize, grid):
    if posX == gridSize and posY == gridSize:
        return 0
    elif posX == gridSize:
        return 1
    elif posY == gridSize:
        return 1
    else:
        return gridPaths(posX+1, posY, gridSize) + gridPaths(posX, posY+1, gridSize)

def main():

    # We will want to memorize values to prevent working 

    print gridPaths(0, 0, 20)

if __name__ == "__main__":
    main()
