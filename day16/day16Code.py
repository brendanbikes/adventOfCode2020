from numpy import prod
import sys

def readInput():
	with open('day16Input.txt', 'r') as f:
		return [x for x in f.read().split('\n\n')]

def part1():
	data = readInput()

	rules, myTicket, nearbyTickets = data
	rules = rules.splitlines()

	#process rules
	text = []
	ranges = []
	for rule in rules:
		t, r = [x.strip() for x in rule.split(':')]
		r = [[int(y) for y in x.split('-')] for x in r.split(' or ')]
		text.append(t)
		ranges.append(r)

	#process ticket
	header, myTicketVals = myTicket.split('\n')
	myTicketVals = [int(x) for x in myTicketVals.split(',')]

	#process nearby tickets

	nearbyTicketVals = [[int(y) for y in x.split(',')] for x in [z for z in nearbyTickets.split('\n')][1:]]

	invalidValues = []
	validValues = []

	validTickets= []
	for ticket in nearbyTicketVals:
		invalidValuesOnTicket = set()
		validValuesOnTicket = set()
		#find invalid values and store them
		for value in ticket:
			i=0
			while value not in validValuesOnTicket and i < len(ranges):
				rangeSet = ranges[i]
				for r in rangeSet:
					if value in list(range(r[0], r[1]+1)):
						validValuesOnTicket.add(value)
				i+=1
			if value not in validValuesOnTicket:
				invalidValuesOnTicket.add(value)


		if not len(invalidValuesOnTicket):
			#valid ticket
			validTickets.append(ticket)


		invalidValues.append(invalidValuesOnTicket)
		validValues.append(validValuesOnTicket)

	print(sum([sum(x) for x in invalidValues]))

	#return list of indices of valid tickets only
	return validTickets, text, ranges, myTicketVals

def findFieldMap(validTickets, text, ranges):
	matches = [] #list of tuples of matches - first elemenent is the rule, second element is column of values that match it
	for i in range(0,len(text)):
		for k in range(0,len(text)):
			#check k column values against rule i
			vals = [x[k] for x in validTickets]
			valids = list(range(ranges[i][0][0], ranges[i][0][1]+1)) + list(range(ranges[i][1][0], ranges[i][1][1]+1))
			#check this set of values against the current rule

			if set(vals).issubset(set(valids)):
				#all values are in set of valid values for this rule
				matches.append(tuple([i, k]))

	uniqueMap = []
	#make the map unique
	while len(uniqueMap) < len(text):
		for i in range(0, len(text)):
			subMatches = [x for x in matches if x[0] == i]
			if len(subMatches) == 1:
				#found a unique match
				uniqueMap.append(subMatches[0])
				#remove elements from map corresponding to rule i or field subMatch[1]
				matches = [x for x in matches if x[0] != i and x[1] != subMatches[0][1]]

	return uniqueMap

def part2(validTickets, text, ranges, myTicketVals):
	fieldMap = findFieldMap(validTickets, text, ranges)

	#find indices that correspond to Departure -- rule indices 0 thru 5
	fieldIndices = [x[1] for x in fieldMap if x[0] in range(0,6)]

	#multiply these values together on my ticket
	departureVals = [x for i, x in enumerate(myTicketVals) if i in fieldIndices]

	print(prod(departureVals))


if __name__ == '__main__':
	validTickets, text, ranges, myTicketVals = part1()

	part2(validTickets, text, ranges, myTicketVals)