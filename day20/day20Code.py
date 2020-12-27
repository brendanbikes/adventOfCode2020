from math import sqrt
import sys
from itertools import permutations
import random
import numpy as np

def readInput():
	tiles = {}
	with open('day20Input.txt', 'r') as f:
		data = [[y for y in x.splitlines()] for x in f.read().split('\n\n')]
	#make a dictionary
	for item in data:
		key = int(item[0][5:9])
		value = item[1:]
		tiles[key] = value

	return tiles


def part1():
	tiles = readInput()

	#gather up all possible edges + flipped edges for all tiles, and map them to the tile ID

	N = len(tiles)
	n = int(sqrt(N))
	q = len([tile for tileID, tile in tiles.items()][0])
	r = len([tile for tileID, tile in tiles.items()][0][0])

	flipNames = ['top', 'bottom', 'left', 'right', 'topFlipped', 'bottomFlipped', 'leftFlipped', 'rightFlipped']

	tileEdgeMap = {}
	edgeTileMap = {}
	
	for tileID, tile in tiles.items():
		top = tile[0]
		bottom = tile[-1]
		left = ''.join([x[0] for x in tile])
		right = ''.join([x[-1] for x in tile])


		topFlipped = top[::-1]
		bottomFlipped = bottom[::-1]
		leftFlipped = left[::-1]
		rightFlipped = right[::-1]

		edgeList = [top, bottom, left, right, topFlipped, bottomFlipped, leftFlipped, rightFlipped]

		tileEdgeMap[tileID] = edgeList

		for edge in edgeList:
			if edge in [key for key in edgeTileMap.keys()]:
				#append tileID to existing item
				value = edgeTileMap[edge]
				value.add(tileID)
				edgeTileMap[edge] = value
			else:
				#new mapping
				value = set([tileID])
				edgeTileMap[edge] = value

	edgePieces = dict()

	grid={}
	gridIDs={}

	for edge, tileIDs in edgeTileMap.items():
		if len(tileIDs) == 1:
			edge = ''.join(list(edge))
			tileID = list(tileIDs)[0]
			#this is an edge piece

			if tileID in [x for x, y in edgePieces.items()]:
				value = edgePieces[tileID]
				value.add(edge)
				edgePieces[tileID] = value
			else:
				edgePieces[tileID] = set([edge])


	#print(edgePieces)

	#identify the corners
	corners = [x for x, y in edgePieces.items() if len(y) == 4]


	#print(corners)
	#print(np.prod(corners))

	#continue assembling the image

	A = {}
	B = {}
	#build a mapping between tiles -- an adjacency matrix A, where A(i,j) is 1 if tiles map to each other, 0 otherwise
	#the B matrix stores the sideOrientations -- how the tiles match at the intersection

	tileIDs = [tileID for tileID, tile in tiles.items()]

	for tileID1 in tileIDs:
		edgeList1 = set(tileEdgeMap[tileID1])

		for tileID2 in tileIDs:
			if tileID1 != tileID2:
				edgeList2 = set(tileEdgeMap[tileID2])

				if edgeList1.intersection(edgeList2):
					#these two tiles share an edge

					#store the shared edge

					sharedEdge = sorted(list(edgeList1.intersection(edgeList2)))[0]

					A[(tileID1, tileID2)] = sharedEdge
					B[(tileID1, tileID2)] = [flipNames[tileEdgeMap[tileID1].index(sharedEdge)], flipNames[tileEdgeMap[tileID2].index(sharedEdge)]]

	#assign one corner to grid - use corners[0]

	piece = corners[0]

	grid[(0,0)] = tiles.get(piece)
	gridIDs[(0,0)] = piece


	#print(grid)

	#print(gridIDs)

	K = 4 * n - 4 #number of edge pieces

	k = 1 #start with coordinate (0, 1)

	previous = piece

	assigned = [previous]


	while k < N:
		i = k // n
		j = k % n

		#print('\n')

		#print(n)
		#print(i, j)

		if (i in range(0,n) and j in [0, n-1]) or (i in [0, n-1] and j in range(0,n)):
			print('edge')
			#this is an edge tile
			neighbors = [gridIDs.get(x) for x in [(i-1, j), (i, j-1)]]
			neighbors = [x for x in neighbors if x]

			print(neighbors)
			print(len(neighbors))

			candidates = [key[0] for key in A.keys() if (key[1] in neighbors and key[0] in [y for y in edgePieces.keys()] and key[0] not in assigned)]#[0]

			filtered=[]
			for candidate in candidates:
				#candidate must connect to all neighbors
				count = 0
				for neighbor in neighbors:
					if (candidate, neighbor) in A:
						count+=1
				if count == len(neighbors):
					filtered.append(candidate)

			candidates = filtered[:]

			print(candidates)

			#pick the first candidate and slot to grid

			grid[(i, j)] = tiles.get(candidates[0])
			gridIDs[(i, j)] = candidates[0]

			assigned.append(candidates[0])

		else:
			#this is not an edge tile
			print('not edge')
			neighbors = [gridIDs.get(x) for x in [(i-1, j), (i, j-1)]]
			neighbors = [x for x in neighbors if x]

			#print(neighbors)
			#print(len(neighbors))

			candidates = [key[0] for key in A.keys() if key[1] in neighbors and key[0] not in assigned]

			filtered=[]
			for candidate in candidates:
				#candidate must connect to all neighbors
				count = 0
				for neighbor in neighbors:
					if (candidate, neighbor) in A:
						count+=1
				if count == len(neighbors):
					filtered.append(candidate)

			candidates = filtered[:]

			#print(candidates)

			#pick the first candidate and slot to grid

			grid[(i, j)] = tiles[candidates[0]]
			gridIDs[(i, j)] = candidates[0]

			assigned.append(candidates[0])

		#print(gridIDs)

		k+=1

	print(B)

	###now go through the grid and convolute each next tile according to how its edges match its previous neighbors

	print('\nBefore rearranging...')
	renderGrid(grid, n, q)

	for i in range(0, n):
	#rearrange the first two tiles in a row to each other
		tileID1 = gridIDs.get((i,0))
		tileID2 = gridIDs.get((i,1))

		tile1 = grid.get((i,0))[:]
		tile2 = grid.get((i,1))[:]

		commonEdge = A.get((tileID1, tileID2))

		#get orientation of pair

		sideOrientation1, sideOrientation2 = B.get((tileID1, tileID2))[:]

		print(sideOrientation1, sideOrientation2)

		#flip/rotate the first tile

		for x in tile1:
			print(x)

		print('\n')

		tile1 = orientTile(tile1, sideOrientation1, 'left')
		tile2 = orientTile(tile2, sideOrientation2, 'right')

		#insert into grid
		grid[(i,0)] = tile1[:]
		grid[(i,1)] = tile2[:]

		#now rotate/flip other tiles in this row successively

		for j in range(2,n):
			print(i, j)
			#initial values
			match = False
			flipped = False
			rotateCounter=0

			while not match:
				thisTile = grid.get((i,j))[:]
				lastTile = grid.get((i,j-1))[:]

				if [x[-1] for x in lastTile] == [x[0] for x in thisTile]:
					match = True
				else:
					#rotate
					if rotateCounter < 4:
						thisTile = rotateCW(thisTile)
						rotateCounter+=1

					elif rotateCounter < 9:
						#flip the tile once and then rotate
						if not flipped:
							thisTile = flipVertical(thisTile)
							flipped = True

						else:
							thisTile = rotateCW(thisTile)
							rotateCounter+=1

					grid[(i, j)] = thisTile[:]

	#the rows are now internally consistent
	#now do horizontal flips of the rows

	renderGrid(grid, n, q)

	allMatch = False

	while not allMatch:

		for i in range (0, n-1):
			rowFlip = False #if false, flip the first row; if true, flip the second row
			match = False

			while not match:
				thisTile = grid.get((i,0))[:]
				nextTile = grid.get((i+1,0))[:]

				if thisTile[-1] == nextTile[0]:
					match = True
				else:
					if not rowFlip:
						#horizontal flip first row
						for j in range(0,n):
							tile = grid.get((i, j))[:]
							tile = flipHorizontal(tile)

							grid[(i, j)] = tile[:]

						rowFlip = True

					else:
						#horizontal flip second row
						for j in range(0, n):
							tile = grid.get((i+1,j))[:]
							tile = flipHorizontal(tile)
							grid[(i+1, j)] = tile[:]

						rowFlip = False

		#check if all row pairs match
		matches = []
		for i in range(0, n-1):
			thisTile = grid.get((i,0))[:]
			nextTile = grid.get((i+1,0))[:]

			if thisTile[-1] != nextTile[0]:
				matches.append(0)

		if len(matches) == 0:
			allMatch = True

	#remove the borders of the tiles
	for key, tile in grid.items():
		tile = [x[1:-1] for x in tile[1:-1]]
		grid[key] = tile

	fullImage = renderGrid(grid, n, q-2)

	#combine the whole image together
	print('\n')
	for row in fullImage:
		print(row)

	#find sea monsters
	seaMonsterPattern = readSeaMonsterPattern()

	seaMonsterIndices = []
	for row in seaMonsterPattern:
		seaMonsterIndices.append([i for i, x in enumerate(row) if x == '#'])

	seaMonsterCount = 0
	flipped = False
	rotationCount = 0

	while seaMonsterCount == 0:

		roughSeas = 0

		for i in range(0,len(fullImage)-2):
			row1 = fullImage[i]
			row2 = fullImage[i+1]
			row3 = fullImage[i+2]

			row1indices = [j for j, x in enumerate(row1) if x == '#']
			row2indices = [j for j, x in enumerate(row2) if x == '#']
			row3indices = [j for j, x in enumerate(row3) if x == '#']

			for k in range(0, len(row1)-len(seaMonsterPattern[0])+1): #possible offsets
				if set([z+k for z in seaMonsterIndices[0]]).issubset(set(row1indices)) and set([z+k for z in seaMonsterIndices[1]]).issubset(set(row2indices)) and set([z+k for z in seaMonsterIndices[2]]).issubset(set(row3indices)):
					#monster found!
					print('monster found')
					seaMonsterCount+=1

		if seaMonsterCount == 0:
			if rotationCount < 4:
				#rotate whole image
				fullImage = rotateCW(fullImage)
				rotationCount+=1

			elif rotationCount < 9:
				#flip and then rotate
				if flipped == False:
					fullImage = flipHorizontal(fullImage)
					flipped = True
				fullImage = rotateCW(fullImage)
				rotationCount+=1

	for row in fullImage:
		print(row)

	seaMonsterSize = 0
	for row in seaMonsterIndices:
		seaMonsterSize += len(row)

	#count of spaces taken by sea monsters
	seaMonsterSpaces = seaMonsterCount * seaMonsterSize

	#rough seas = total count minus seaMonsterSpaces

	totalCount = 0
	for row in fullImage:
		totalCount += len([i for i, x in enumerate(list(row)) if x == '#'])

	print('There were {} tiles of rough seas encountered, and {} sea monsters'.format(totalCount-seaMonsterSpaces, seaMonsterCount))


def readSeaMonsterPattern():
	with open('seaMonsterPattern.txt', 'r') as f:
		return f.read().splitlines()

def renderGrid(grid, n, q):
	#render the grid

	#print(grid)

	arrayGrid = []

	for i in range(0, n):
		arrayGrid.append([])
		for j in range(0, n):
			arrayGrid[i].append([])
			#slot in tile
			arrayGrid[i][j] = grid.get((i, j))

	print('\n')
	fullMatrix = []
	for rowOfTiles in arrayGrid:
		#print(rowOfTiles)
		print('\n')
		for i in range(0, q):
			outerRow = [tile[i] for tile in rowOfTiles]
			print(outerRow)
			fullMatrix.append(''.join(outerRow))

	return fullMatrix


def orientTile(tile, sideOrientation, position):

	if sideOrientation == 'right' and position == 'left':
		#do nothing
		return tile

	elif sideOrientation == 'left' and position == 'left':
		#flip tile on vertical axis
		return flipVertical(tile)

	elif sideOrientation == 'top' and position == 'left':
		#rotate CW 90 degrees
		return rotateCW(tile)

	elif sideOrientation == 'bottom' and position == 'left':
		#transpose the tile
		tile = [''.join(x) for x in np.array([list(x) for x in tile]).T.tolist()]
		return tile

	elif sideOrientation == 'rightFlipped' and position == 'left':
		#flip the tile on horizontal axis
		return flipHorizontal(tile)

	elif sideOrientation == 'leftFlipped' and position == 'left':
		#flip tile on vertical and horizontal axis
		return flipHorizontal(flipVertical(tile))

	elif sideOrientation == 'topFlipped' and position == 'left':
		#flip tile on vertical axis and rotate CW 90 degrees
		return rotateCW(flipVertical(tile))

	elif sideOrientation == 'bottomFlipped' and position == 'left':
		##flip tile on vertical axis and rotate CCW 90 degrees
		return rotateCCW(flipVertical(tile))

	elif sideOrientation == 'right' and position == 'right':
		#flip tile vertically
		return flipVertical(tile)

	elif sideOrientation == 'left' and position == 'right':
		#do nothing
		return tile

	elif sideOrientation == 'top' and position == 'right':
		#transpose the tile
		tile = [''.join(x) for x in np.array([list(x) for x in tile]).T.tolist()]
		return tile

	elif sideOrientation == 'bottom' and position == 'right':
		#rotate tile 90 CW
		return rotateCW(tile)

	elif sideOrientation == 'rightFlipped' and position == 'right':
		#flip tile on vertical and horizontal axis
		return flipHorizontal(flipVertical(tile))

	elif sideOrientation == 'leftFlipped' and position == 'right':
		#flip tile on horizontal axis
		return flipHorizontal(tile)

	elif sideOrientation == 'topFlipped' and position == 'right':
		#rotate tile 90 CCW
		return rotateCCW(tile)

	elif sideOrientation == 'bottomFlipped' and position == 'right':
		#flip tile on vertical axis and rotate 90 CW
		return rotateCW(flipVertical(tile))

def flipVertical(tile):
	return [x[::-1] for x in tile]

def flipHorizontal(tile):
	tile.reverse()
	return tile

def rotateCW(tile):
	tile.reverse()
	tile = [''.join([x[i] for x in tile]) for i in range(0,len(tile))]

	return tile

def rotateCCW(tile):
	tile = flipHorizontal([''.join(x) for x in np.array([list(x) for x in tile]).T.tolist()])

	return tile


if __name__ == "__main__":
	part1()
	#part2()