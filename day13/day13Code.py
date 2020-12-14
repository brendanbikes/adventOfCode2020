from numpy import prod, linalg as la
import sys


def readInput():
	with open('day13input.txt', 'r') as f:
		return f.read().splitlines()

def gcdExtended(a, b):
	if a == 0:
		return b, 0, 1

	gcd, x1, y1 = gcdExtended(b%a, a)

	x = y1 - (b//a) * x1
	y = x1

	return gcd, x, y

def part1():
	data = readInput()

	departure = int(data[0])
	busHeadways = data[1].split(',')

	filtered = []
	for x in busHeadways:
		if x != 'x':
			filtered.append(int(x))

	busHeadways = filtered[:]

	nextBusWaitTimes = []

	for busHeadway in busHeadways:
		print(busHeadway)
		print(departure)
		mod = departure % busHeadway
		nextBusWaitTimes.append(busHeadway - mod if mod > 0 else 0)

	minWaitTime = min(nextBusWaitTimes)
	indexMin = min(range(len(nextBusWaitTimes)), key=nextBusWaitTimes.__getitem__)
	bestBus = busHeadways[indexMin]

	print('This is the minimum waiting time {}, for bus route {}'.format(minWaitTime, bestBus))
	print('This is the answer: {}'.format(bestBus * minWaitTime))


def part2():
	data = readInput()

	busHeadways = data[1].split(',')

	indices = list(range(len(busHeadways)))

	#find the x's - this gives the indices of the x values
	xIndices = [i for i, e in enumerate(busHeadways) if e == 'x']

	i = 0
	filteredIndices = []
	filteredHeadways = []
	for headway in busHeadways:
		if headway != 'x':
			filteredHeadways.append(int(headway))
			filteredIndices.append(i)
		i+=1


	#sort real bus headways and indices
	zipped = zip(filteredHeadways, filteredIndices)
	sortedPairs = sorted(zipped, reverse = True)
	tuples = zip(*sortedPairs)

	sortedHeadways, sortedIndices = [list(tuple) for tuple in tuples]

	sortedA = [x-y for x, y in zip(sortedHeadways, sortedIndices)]

	#print(sortedA)

	#print(sortedHeadways)
	#print(sortedIndices)

	#do Chinese Remainder Theorem
	#compute N - product of headways
	N = prod(sortedHeadways)

	Y = []
	S = []

	for i in range(0,len(sortedHeadways)):
		temp = sortedHeadways[:]
		temp.pop(i)
		print(temp)
		y_i = prod(temp)
		Y.append(y_i)
		gcd, r_i, s_i = gcdExtended(sortedHeadways[i], y_i)
		S.append(s_i)

	#
	sol = sum([x*y*z for x, y, z in zip(sortedA, Y, S)])

	print(sol)
	print(sol % N)














	###brute force below here

	# #initial timepoint
	# t = sortedHeadways[0] - sortedIndices[0]

	# i=1
	# matched = 0 #initialize

	# while matched < len(sortedHeadways)-1:
	# 	#try the remaining headways
	# 	matched=0
	# 	#print(t)

	# 	for headway, index in zip(sortedHeadways[1:], sortedIndices[1:]):
	# 		if (t + index) % headway != 0:
	# 			#don't keep trying -- need to increase initial timepoint
	# 			t+=sortedHeadways[0]
	# 			break
	# 		else:
	# 			matched+=1

	# #timepoint and all differences mod to their headways
	# print('This is the desired timepoint: {}'.format(t))


if __name__ == "__main__":
	#part1()
	part2()