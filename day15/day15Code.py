def part2():

	initialNumbers = [0,14,1,3,7,9]

	#sequence = initialNumbers[:]

	t = len(initialNumbers)

	mostRecentIndices = {}
	secondMostRecentIndices = {}

	for i, v in enumerate(initialNumbers):
		mostRecentIndices['{}'.format(v)] = i+1

	#seed
	current = initialNumbers[-1]

	maxTime = 30000000

	while t < maxTime:
		#assess number at time t

		mostRecentIndex = mostRecentIndices.get('{}'.format(current), '')
		secondMostRecentIndex = secondMostRecentIndices.get('{}'.format(current), '')

		if mostRecentIndex==t and bool(secondMostRecentIndex):
			#this number has been seen before
			next = t - secondMostRecentIndex

		elif mostRecentIndex==t and not secondMostRecentIndex:
			#this number was new
			next = 0

		#update indices for the next number

		if not secondMostRecentIndices.get('{}'.format(next), '') and not mostRecentIndices.get('{}'.format(next), ''):
			#totally new number
			mostRecentIndices['{}'.format(next)] = t + 1
		else:
			#not a new number
			secondMostRecentIndices['{}'.format(next)] = mostRecentIndices['{}'.format(next)]
			mostRecentIndices['{}'.format(next)] = t + 1

		#sequence.append(next)

		#increment
		t+=1
		current = next

	print('This is the last number spoken: {}'.format(current))


def part1():

	initialNumbers = [0,14,1,3,7,9]

	spokenOrder = initialNumbers[:]

	t = len(initialNumbers)
	while t < 30000000:
		t+=1
		if spokenOrder[-1] not in set(spokenOrder[:-1]):
			next = 0
		else:
			next = (t-1) - max([i+1 for i, v in enumerate(spokenOrder[:-1]) if v == spokenOrder[-1]])
		spokenOrder.append(next)
		print(t)
		
	#print(spokenOrder)
	print('This is the 2020th number spoken: {}'.format(spokenOrder[-1]))


if __name__ == "__main__":
	#part1()
	part2()