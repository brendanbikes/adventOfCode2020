import re
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

def readInput():
	with open('day7input.txt', 'r') as f:
		data = sorted(f.read().splitlines())
	return data

def parseRule(rule):
	outerColor, contents = rule.replace('.', '').split(' bags contain ')
	contents = contents.split(', ')
	containedBags = []

	dictItem = {}
	containedBags = {}

	for item in contents:
		if item == 'no other bags':
			break
		else:
			item = item.split(' ')
			number = int(item[0])
			color = item[1] + ' ' + item[2]
			containedBags['{}'.format(color)] = number

	dictItem['{}'.format(outerColor)] = containedBags

	return dictItem

def explodeRulesPart1(rules):
	colors = [x for x, y in rules.iteritems()]

	terminalColors = [x if not bool(y) else None for x, y in rules.iteritems()]

	newTerminalColors=[]
	for x in terminalColors:
		if x != None:
			newTerminalColors.append(x)

	numColors = len(colors)

	bagsWithShinyGold=set()

	for color in colors:
		baglist=[]
		if not bool(rules['{}'.format(color)]):
			bagList.append(color)
		else:
			bagList = [x for x, y in rules['{}'.format(color)].iteritems()]
			#bagList = [item for sublist in bagList for item in sublist]

			while not set(bagList).issubset(set(newTerminalColors)):
				if 'shiny gold' in bagList:
					bagsWithShinyGold.add(color)

				newBagList = []
				for innerColor in bagList:
					if innerColor not in newTerminalColors:

						temp=[x for x, y in rules['{}'.format(innerColor)].iteritems()]
						#temp=[item for sublist in temp for item in sublist]
						newBagList += temp

				bagList = newBagList

	print(len(bagsWithShinyGold))


def expandBagList(color, rules, count=0):
	#get list of expanded colors
	#add list of expanded colors to list
	#if the list is not a subset of terminal colors, call function recursisvely
	insideColors = [y*[x] for x, y in rules['{}'.format(color)].iteritems()]
	insideColors = [item for sublist in insideColors for item in sublist] #flatten the list

	bagList = []

	count+=1
	if not insideColors:
		bagList.append(color)
	else:
		for color in insideColors:
			results, count = expandBagList(color, rules, count)
			for item in results:
				bagList.append(item)

	return bagList, count


def part1():
	data = readInput()


	rules = {}
	for rule in data:
		dictItem = parseRule(rule)
		rules.update(dictItem)

	#print(rules)

	explodeRulesPart1(rules)


def part2():
	data = readInput()


	rules = {}
	for rule in data:
		dictItem = parseRule(rule)
		rules.update(dictItem)

	#print(rules)

	#explodeRulesPart2(rules)

	bagList, bagCount = expandBagList('shiny gold', rules, 0)
	#print(bagList)
	print(bagCount-1) #don't count the outermost bag


if __name__ == "__main__":
	part1()
	part2()