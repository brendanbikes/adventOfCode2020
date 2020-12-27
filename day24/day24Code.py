import sys

def readInput():
	with open('day24Input.txt', 'r') as f:
		return f.read().splitlines()

def part1():
	data = readInput()

	#initialize tile dict
	tiles = {}

	for command in data:
		#starting coordinate
		i = 0
		j = 0
		while command:
			if i % 2 == 0:
				#even
				even = True
			else:
				even = False

			if command[0:1] == 'e':
				j+=1
				command = command[1:]

			elif command[0:2] == 'se':
				if even:
					i+=1
				else:
					i+=1
					j+=1

				command = command[2:]

			elif command[0:2] == 'sw':
				if even:
					i+=1
					j-=1
				else:
					i+=1
				command = command[2:]

			elif command[0:1] == 'w':
				j-=1
				command = command[1:]

			elif command[0:2] == 'nw':
				if even:
					i-=1
					j-=1
				else:
					i-=1
				command = command[2:]

			elif command[0:2] == 'ne':
				if even:
					i-=1
				else:
					i-=1
					j+=1
				command = command[2:]

		#flip tile i,j -- white is 0, black is 1
		if tiles.get((i,j), 0) == 0:
			tiles[(i,j)] = 1
		else:
			tiles[(i,j)] = 0

	#count black tiles
	print('There are {} black tiles'.format(len([x for x in tiles.values() if x == 1])))

	return tiles


def part2():
	tiles = part1()

	#number of iterations
	n = 100

	for i in range(0,n):
		#first determine current floor boundary and add a layer all around it
		minX = min([x[1] for x in tiles.keys()])
		maxX = max([x[1] for x in tiles.keys()])
		minY = min([x[0] for x in tiles.keys()])
		maxY = max([x[0] for x in tiles.keys()])

		#initialize additional grid layer
		for q in range(minY-1, maxY+2):
			for r in range(minX-1, maxX+2):
				if (q,r) not in tiles.keys():
					tiles[(q,r)]=0

		#create new copy of tiles to receive edits
		tilesNew = tiles.copy()

		#iterate through the tiles and update
		for tile, state in tiles.items():
			i = tile[0]
			j = tile[1]

			if i % 2 == 0:
				neighbors = [(i-1, j-1), (i-1, j), (i, j+1), (i+1, j), (i+1, j-1), (i, j-1)]
			else:
				neighbors = [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i, j-1)]

			blackCount = 0
			for neighbor in neighbors:
				if tiles.get(neighbor) == 1:
					blackCount+=1

			if state == 1 and (blackCount == 0 or blackCount > 2):
				state = 0
			elif state == 0 and blackCount == 2:
				state = 1

			#set tile in grid copy
			tilesNew[tile] = state

		#copy tile state back
		tiles = tilesNew.copy()

	#how many black tiles are there now?
	print('There are {} black tiles'.format(len([x for x in tiles.values() if x == 1])))


if __name__ == '__main__':
	#part1()
	part2()