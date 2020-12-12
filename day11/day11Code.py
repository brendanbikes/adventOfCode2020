import os
import sys
import time
import copy
from pandas import *

pandas.set_option("display.max_rows", None, "display.max_columns", None)

def clear():
	os.system('clear')

def readInput():
	with open('day11input.txt', 'r') as f:
		return [[y for y in x] for x in f.read().splitlines()]

def checkSightline(sightline):
	#print(sightline)
	if sightline:
		for seat in sightline:
			#check seats in order of closeness
			if seat == '#':
				#first seat found is occupied
				return 1

			elif seat == 'L':
				#first seat found is empty
				return 0
		#encountered nothing but empty space
		return 0
	else:
		#print(0)
		return 0

def part1():
	data = readInput()

	numCols = len(data[0])
	numRows = len(data)
	jumps = [-1, 0, 1]

	#initialize array
	seats = data[:]

	#dummy variable to get the loop started
	numChanged = 1

	while numChanged > 0:
		#initialize next step
		next = copy.deepcopy(seats)

		numChanged = 0

		#clear output
		#clear()

		#pretty print the matrix
		#print(DataFrame(seats))

		for row in range(0,numRows):
			for col in range(0, numCols):

				if seats[row][col] == '.':
					#skip testing this cell -- it's an empty space with no seat
					continue

				adjacentOccupied = 0

				#non-empty space -- check adjacencies
				for x in [row + jump for jump in jumps]:
					for y in [col + jump for jump in jumps]:
						
						if x == row and y == col:
							#skip this -- it's the seat we're checking aroudnd
							continue

						if x < 0 or x == len(data) or y < 0 or y == len(data[0]):
							#skip this -- beyond the boundary
							continue

						if seats[x][y] == '#':
							#occupied
							adjacentOccupied+=1

				if seats[row][col] == 'L' and adjacentOccupied == 0:
					#empty seat and no one around it -- fill it
					next[row][col] = '#'
					numChanged += 1

				elif seats[row][col] == '#' and adjacentOccupied >= 4:
					#occupied seat and too many people around -- vacate it
					next[row][col] = 'L'
					numChanged += 1

		#update step
		seats = copy.deepcopy(next)
		time.sleep(0.05)

	#count occupied seats
	finalOccupied = 0
	for row in seats:
		for col in row:
			if col == '#':
				finalOccupied+=1

	print('There are {} occupied seats.'.format(finalOccupied))


def part2():

	data = readInput()

	numCols = len(data[0])
	numRows = len(data)
	jumps = [-1, 0, 1]

	#initialize array
	seats = data[:]

	#dummy variable to get the loop started
	numChanged = 1

	while numChanged > 0:
		#initialize next step
		next = copy.deepcopy(seats)

		numChanged = 0

		#clear output
		clear()

		#pretty print the matrix
		print(DataFrame(seats))

		for row in range(0,numRows):
			for col in range(0, numCols):

				if seats[row][col] == '.':
					#skip testing this cell -- it's an empty space with no seat
					continue

				sightlineOccupied = 0

				#non-empty space -- check sightlines
				#left
				temp = seats[row][0:col]
				temp.reverse()
				sightlineOccupied += checkSightline(temp)

				#right
				temp = seats[row][col:]
				temp.pop(0)

				sightlineOccupied += checkSightline(temp)

				#top - all rows above row x in column y
				temp = [seats[i][col] for i in range(0,row)]
				temp.reverse()

				sightlineOccupied += checkSightline(temp)

				#bottom - all rows below row x in column y
				temp=list(range(row,numRows))
				temp.pop(0)

				sightlineOccupied += checkSightline([seats[i][col] for i in temp])

				#NW diagonal
				i = 1
				NWdiag = []
				while row-i >=0 and col-i >= 0:
					try:
						NWdiag.append(seats[row-i][col-i])
					except IndexError as e:
						break
					i+=1

				sightlineOccupied += checkSightline(NWdiag)

				#NE diagonal
				i = 1
				NEdiag = []
				while row-i >=0:
					try:
						NEdiag.append(seats[row-i][col+i])
					except IndexError as e:
						break
					i+=1

				sightlineOccupied += checkSightline(NEdiag)

				#SW diagonol
				i = 1
				SWdiag = []
				while col-i >= 0:
					try:
						SWdiag.append(seats[row+i][col-i])
					except IndexError as e:
						break
					i+=1
				
				sightlineOccupied += checkSightline(SWdiag)

				#SE diagonal
				i=1
				SEdiag = []
				while i:
					try:
						SEdiag.append(seats[row+i][col+i])
					except IndexError as e:
						break
					i+=1

				sightlineOccupied += checkSightline(SEdiag)


				if seats[row][col] == 'L' and sightlineOccupied == 0:
					#empty seat and no one around it -- fill it
					next[row][col] = '#'
					numChanged += 1

				elif seats[row][col] == '#' and sightlineOccupied >= 5:
					#occupied seat and too many people around -- vacate it
					next[row][col] = 'L'
					numChanged += 1

		#update step
		seats = copy.deepcopy(next)
		time.sleep(0.05)

	#count occupied seats
	finalOccupied = 0
	for row in seats:
		for col in row:
			if col == '#':
				finalOccupied+=1

	print('There are {} occupied seats.'.format(finalOccupied))


if __name__ in "__main__":
	#part1()
	part2()