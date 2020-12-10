from itertools import groupby
import sys

def readInput():
	with open('day10input.txt', 'r') as f:
		data = f.read().splitlines()
	return sorted([int(x) for x in data])


def part1(data):

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



def recur(data, currentPath=None, joltage=0, allowedJumps=[1,2,3]):
	allPaths=[]

	if currentPath is None:
		currentPath=[]

	currentPath.append(joltage)

	nextAdapters=[]
	possible = [joltage + x for x in allowedJumps]

	for x in possible:
		if x in data:
			nextAdapters.append(x)

	if nextAdapters:
		for nextAdapter in nextAdapters:
			allPaths.extend(recur(data, currentPath[:], nextAdapter))
	else:
		#we've reached a terminal node
		allPaths.append(currentPath)
	return allPaths

def part2(data):
	paths = recur(data)
	#print(paths)
	print(len(paths))

if __name__ == "__main__":
	data = readInput()
	#part1(data)

	part2(data)