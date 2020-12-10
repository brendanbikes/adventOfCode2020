from itertools import groupby
import sys
import numpy as np
import scipy.linalg as la


np.set_printoptions(suppress=True, linewidth=np.nan, threshold=np.nan)

def readInput():
	with open('day10input.txt', 'r') as f:
		data = f.read().splitlines()
	return sorted([int(x) for x in data])

def recur(data, pathCount=0, currentPath=None, joltage=0, allowedJumps=[1,2,3]):

	if currentPath is None:
		currentPath=[]
	currentPath.append(joltage)

	nextAdapters=[]
	possible = [currentPath[-1] + x for x in allowedJumps]

	for x in possible:
		if x in data:
			nextAdapters.append(x)

	if nextAdapters:
		for nextAdapter in nextAdapters:
			pathCount = recur(data, pathCount, currentPath[:], nextAdapter)
	else:
		#we've reached a terminal node
		pathCount+=1
	return pathCount


def matrix(data, allowedJumps=[1,2,3]):
	#treat numbers as variables
	matrix = np.zeros((len(data)+1, len(data)+1))

	indexes = range(0,len(data)+1)
	#add in the 0 node
	data = [0] + data
	for number in data:
		for jump in allowedJumps:
			if number+jump in data:
				matrix[data.index(number), data.index(number+jump)] = 1

	pathCount=0
	for i in range(0,len(data)):
		#count the number of paths of length i between the start and end points
		product = np.linalg.matrix_power(matrix, i+1)
		pathCount += product[0,indexes[-1]] #must reach the node for largest adapter -- the built-in adapter is an automatic +3 jolts beyond this, and can't be reached from any other node

	return pathCount

def part1(data):

	print(data)

	differences = []
	differences.append(data[0])

	for i in range(1,len(data)):
		differences.append(data[i]-data[i-1])

	differences.append(3) #account for the built-in adapter

	differences = sorted(differences)

	print(differences)

	frequencies = [len(list(group)) for key, group in groupby(differences)]
	print(frequencies)
	print(frequencies[0] * frequencies[1])


def part2(data):

	#pathCountRecur = recur(data)
	#print(pathCountRecur)

	pathCountMatrix=matrix(data)
	print(int(pathCountMatrix))

if __name__ == "__main__":
	data = readInput()
	#part1(data)

	part2(data)