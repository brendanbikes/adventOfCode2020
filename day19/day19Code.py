import re
import sys

def readInput():
	with open('day19InputPart2.txt', 'r') as f:
		return [x.splitlines() for x in f.read().split('\n\n')]

def part1():
	rules, strings = readInput()

	#read the rules into a dictionary
	ruleDict = {}
	for rule in rules:
		key, value = rule.split(':')
		#if '|' in value:
			#value = [[y for y in x.strip().split(' ')] for x in value.split('|')]
		#else:
			#value = [x.replace('"', '') for x in value.strip().split(' ')]

		value = value.replace('"', '').strip()

		ruleDict[int(key)] = value
	
	parsedRules = parseRules(ruleDict)

	count = 0
	for string in strings:
		#print(parsedRules[0])
		if re.fullmatch(r'^{}\Z'.format(parsedRules[0]), string):
			count+=1

	print(count)


def part2():
	rules, strings = readInput()

	#read the rules into a dictionary
	ruleDict = {}
	for rule in rules:
		key, value = rule.split(':')

		value = value.replace('"', '').strip()

		ruleDict[int(key)] = value

	parsedRule42 = parseRule(ruleDict, ruleNum=42)

	###rule 8 matches integer repetitions of rule 42

	parsedRule31 = parseRule(ruleDict, ruleNum=31)

	###rule 11 matches 42 then 31 OR 42 42 31 31 OR 42 42 42 31 31 31

	#rebuild the rules for 8 and 11 - allow 10 integer repetitions

	newRule8 = parsedRule42
	for i in range(2,11):
		newRule8 += '|' + parsedRule42*i

	newRule8 = '(' + newRule8 + ')'

	newRule11 = parsedRule42 + parsedRule31
	for i in range(2,11):
		newRule11 += '|' + parsedRule42*i + parsedRule31*i
	newRule11 = '(' + newRule11 + ')'

	parsedRules = parseRulesPart2(ruleDict, newRule8, newRule11)

	print(parsedRules[0])

	count = 0
	matchedStrings = []
	for string in strings:
		#print(parsedRules[0])
		if re.fullmatch(r'^{}\Z'.format(parsedRules[0]), string):
			count+=1
			matchedStrings.append(string)

	print(count)
	#print(matchedStrings)

def parseRulesPart2(ruleDict, newRule8, newRule11):
	parsedRules = {}

	for key, value in ruleDict.items():
		parsedRule = parseRulePart2(ruleDict, newRule8, newRule11, key)
		if parsedRule[0] == '(':
			parsedRule = parsedRule[1:-1]
		parsedRules[key] = parsedRule

	return parsedRules


def parseRules(ruleDict):
	parsedRules = {}

	for key, value in ruleDict.items():
		parsedRule = parseRule(ruleDict, key)
		if parsedRule[0] == '(':
			parsedRule = parsedRule[1:-1]
		parsedRules[key] = parsedRule

	return parsedRules

def parseRule(ruleDict, ruleNum=0):
	parsedRule = ''

	try:
		rule = ruleDict[ruleNum]

		if not rule:
			return

		if rule == 'a' or rule == 'b':
			parsedRule = rule

		else:
			if '|' in rule:
				subRules = rule.split(' | ')
				parsedRule = parsedRule + "("
				for i, subRule in enumerate(subRules):
					nums = subRule.split(' ')
					for num in nums:
						parsedRule += parseRule(ruleDict, int(num))
					if i < len(subRules)-1:
						parsedRule += '|'
				parsedRule += ')'
			else:
				nums = rule.split(' ')
				parsedRule += '('
				for num in nums:
					parsedRule += parseRule(ruleDict, int(num))
				parsedRule += ')'
		
		return parsedRule
	except TypeError as e:
		print('Hit a loop -- exit')
		return

def parseRulePart2(ruleDict, newRule8, newRule11, ruleNum=0):
	parsedRule = ''

	if ruleNum == 8:
		return newRule8
	elif ruleNum == 11:
		return newRule11

	try:
		rule = ruleDict[ruleNum]

		if not rule:
			return

		if rule == 'a' or rule == 'b':
			parsedRule = rule

		else:
			if '|' in rule:
				subRules = rule.split(' | ')
				parsedRule = parsedRule + "("
				for i, subRule in enumerate(subRules):
					nums = subRule.split(' ')
					for num in nums:
						parsedRule += parseRulePart2(ruleDict, newRule8, newRule11, int(num))
					if i < len(subRules)-1:
						parsedRule += '|'
				parsedRule += ')'
			else:
				nums = rule.split(' ')
				parsedRule += '('
				for num in nums:
					parsedRule += parseRulePart2(ruleDict, newRule8, newRule11, int(num))
				parsedRule += ')'
		
		return parsedRule
	except TypeError as e:
		print('Hit a loop -- exit')
		return


if __name__ == "__main__":
	#part1()
	part2()