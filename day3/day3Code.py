import numpy as np
import sys

def readInput():
	with open('day3input.txt', 'r') as f:
		grid = f.read().splitlines()

	#extend the grid to the right a bunch
	newGrid=[]
	for row in grid:
		row = row*1000
		newGrid.append(row)
	return newGrid

def process():
	grid = readInput()
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

	rows = len(grid)
	columns = len(grid[0])

	treeCountProduct=1
	for pair in slopes:
		slope_x, slope_y = pair
		i_x = 0
		i_y = 0
		treeCount = 0
		while i_x <= columns-1 and i_y <= rows-1:
			#detect tree
			if grid[i_y][i_x] == '#':
				treeCount+=1
			#increment position
			i_x+=slope_x
			i_y+=slope_y

		print('Found {} trees.'.format(treeCount))
		treeCountProduct*=treeCount

	print('This is the product of all tree counts: {}'.format(treeCountProduct))

if __name__ == "__main__":
	process()