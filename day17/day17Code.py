import sys

def readInput():
	with open('day17Input.txt', 'r') as f:
		return [[y for y in x] for x in f.read().splitlines()]

def part1():
	data = readInput()

	n = 6 #number of iterations

	grid = {}

	#initialize values into dict

	for i, row in enumerate(data):
		for k, cellValue in enumerate(row):
			key = (k, i, 0)
			grid[key] = cellValue

	t = 1
	while t <= n:
		#iterate grid at time t

		activeCells = 0
		for cell, state in grid.items():
			if state == '#':
				activeCells += 1

		print('There are {} active cells in the grid.'.format(activeCells))

		#pad the grid in all directions by 1, and set these values to inactive - .
		#get the minX,maxX,minY,maxY,minZ,maxZ

		minX = min([key[0] for key, value in grid.items()])
		maxX = max([key[0] for key, value in grid.items()])
		minY = min([key[1] for key, value in grid.items()])
		maxY = max([key[1] for key, value in grid.items()])
		minZ = min([key[2] for key, value in grid.items()])
		maxZ = max([key[2] for key, value in grid.items()])

		#generate new tuples to set to inactive
		for x in range(minX-1, maxX+2):
			for y in range(minY-1, maxY+2):
				for z in range(minZ-1, maxZ+2):
					if not grid.get((x, y, z), ''):
						grid[(x, y, z)] = '.'
		
		#create new copy of grid -- this copy will receive updates
		newGrid = grid.copy()

		#if cell is active and 2-3 active neighbors, stays active; otherwise if active, becomes inactive
		#if cell is inactive and 3 neighbors are active, it becomes active; otherwise if inactive, stays inactive
		
		for cell, state in grid.items():
			#get the neighbors of the cell
			xVals = [cell[0]-1, cell[0], cell[0]+1]
			yVals = [cell[1]-1, cell[1], cell[1]+1]
			zVals = [cell[2]-1, cell[2], cell[2]+1]

			activeNeighbors = 0

			for x in xVals:
				for y in yVals:
					for z in zVals:
						#print('Checking neighbor at coordinate {}:'.format((x, y, z)))

						if x == cell[0] and y == cell[1] and z == cell[2]:
							#this is the cell being analyzed -- skip it
							continue

						if grid.get((x, y, z), '') == '#':
							#neighbor is active
							activeNeighbors += 1

			#update the current cell in the new grid copy
			if activeNeighbors not in [2, 3] and state == '#':
				newGrid[cell] = '.'

			elif activeNeighbors == 3 and state == '.':
				newGrid[cell] = '#'

		# copy newGrid back to grid

		grid = newGrid.copy()

		t += 1
	
	#count the active cells
	activeCells = 0
	for cell, state in grid.items():
		if state == '#':
			activeCells += 1

	print('There are {} active cells in the grid.'.format(activeCells))


def part2():
	#4-D version
	data = readInput()

	n = 6 #number of iterations

	grid = {}

	#initialize values into dict

	for i, row in enumerate(data):
		for k, cellValue in enumerate(row):
			key = (k, i, 0, 0)
			grid[key] = cellValue

	t = 1
	while t <= n:
		#iterate grid at time t

		activeCells = 0
		for cell, state in grid.items():
			if state == '#':
				activeCells += 1

		print('There are {} active cells in the grid.'.format(activeCells))

		#pad the grid in all directions by 1, and set these values to inactive
		minX = min([key[0] for key, value in grid.items()])
		maxX = max([key[0] for key, value in grid.items()])
		minY = min([key[1] for key, value in grid.items()])
		maxY = max([key[1] for key, value in grid.items()])
		minZ = min([key[2] for key, value in grid.items()])
		maxZ = max([key[2] for key, value in grid.items()])
		minW = min([key[3] for key, value in grid.items()])
		maxW = max([key[3] for key, value in grid.items()])

		#generate new tuples to set to inactive
		for x in range(minX-1, maxX+2):
			for y in range(minY-1, maxY+2):
				for z in range(minZ-1, maxZ+2):
					for w in range(minW-1, maxW+2):
						if not grid.get((x, y, z, w), ''):
							grid[(x, y, z, w)] = '.'

		#create new copy of grid -- this copy will receive updates
		newGrid = grid.copy()

		#if cell is active and 2-3 active neighbors, stays active; otherwise if active, becomes inactive
		#if cell is inactive and 3 neighbors are active, it becomes active; otherwise if inactive, stays inactive

		for cell, state in grid.items():
			#get the neighbors of the cell
			xVals = [cell[0]-1, cell[0], cell[0]+1]
			yVals = [cell[1]-1, cell[1], cell[1]+1]
			zVals = [cell[2]-1, cell[2], cell[2]+1]
			wVals = [cell[3]-1, cell[3], cell[3]+1]

			activeNeighbors = 0

			for x in xVals:
				for y in yVals:
					for z in zVals:
						for w in wVals:
							if x == cell[0] and y == cell[1] and z == cell[2] and w == cell[3]:
								#this is the cell being analyzed -- skip it
								continue

							if grid.get((x, y, z, w), '') == '#':
								#neighbor is active
								activeNeighbors += 1

			#update the current cell in the new grid copy
			if activeNeighbors not in [2, 3] and state == '#':
				newGrid[cell] = '.'

			elif activeNeighbors == 3 and state == '.':
				newGrid[cell] = '#'

		#copy newGrid back to grid

		grid = newGrid.copy()

		t += 1

	#count the active cells
	activeCells = 0
	for cell, state in grid.items():
		if state == '#':
			activeCells += 1

	print('There are {} active cells in the grid.'.format(activeCells))

if __name__ == '__main__':
	#part1()
	part2()

