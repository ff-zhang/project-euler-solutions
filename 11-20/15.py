"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

length = 20

lattice = [[0 for j in range(length+1)] for i in range(length+1)]

lattice[0][0] = 1
for i in range(len(lattice)):
    for j in range(len(lattice)):
        if i:
            lattice[i][j] += lattice[i-1][j]

        if j:
            
            lattice[i][j] += lattice[i][j-1]

print(lattice[length][length])