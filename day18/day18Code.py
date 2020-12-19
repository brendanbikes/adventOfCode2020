import sys
from numpy import prod

def readInput():
	with open('day18Input.txt', 'r') as f:
		return [x.split(' ') for x in f.read().replace('((', '( (').replace('))', ') )').splitlines()]


def parseParens(equation):
	#returns list of tuples of boundaries of subequations, in the order in which to be evaluated
	parens = []
	for i, group in enumerate(equation):
		if group[0] == '(' or group[-1] == ')':
			parens.append((i, group))

	parensPairs = []
	parensCopy = parens[:]

	while len(parensCopy) > 0:
		for k, paren in enumerate(parens):
			if paren[1][0] == '(' and parens[k+1][1][-1] == ')':
				#this is a consecutive pair -- this list will build out innermost to outermost expressions
				parensPairs.append((paren[0], parens[k+1][0]))
				#pop out of parensCopy
				parensCopy = [x for x in parensCopy if x[0] not in [paren[0], parens[k+1][0]]]

		parens = parensCopy[:]

	#add layer
	parensPairsDepth = []
	for parensPair in parensPairs:
		depth = len([x for x in parensPairs if x[0] < parensPair[0] and x[1] > parensPair[1]])
		parensPairsDepth.append((parensPair[0], parensPair[1], depth))

	return parensPairsDepth

def evaluate(expression):
	#print('evaluating expression {}'.format(expression))

	result = 0
	for i, char in enumerate(expression):
		#ignore parentheses -- this is a subexpression
		char = char.strip('()')
		try:
			#if we encounter a number, apply the last operator to the current result
			num = int(char)

			if not result:
				result = num
			else:
				if lastOperator == '+':
					result += num
				elif lastOperator == '*':
					result *= num

		except ValueError as e:
			if char == '+':
				lastOperator = '+'
			elif char == '*':
				lastOperator = '*'
	return result

def evaluatePart2(expression):
	result = 0

	temp = []

	while '*' in expression:
		i = expression.index('*')
		#divider
		temp.append(expression[0:i])
		expression = expression[i+1:]

	temp.append(expression)

	print(temp)

	S = []

	for x in temp:
		S.append(evaluate(x))

	return prod(S)

def parseEquationPart2(equation):
	parensPairs = parseParens(equation)

	#flatten the equation
	while parensPairs:
		pair = [x for x in parensPairs if x[2] == max(x[2] for x in parensPairs)][0]
		#evaluate 1 subexpression in innermost layer
		subResult = evaluatePart2(equation[pair[0]:pair[1]+1])
		equation = equation[0:pair[0]] + [str(subResult)] + equation[pair[1]+1:]

		parensPairs = parseParens(equation)

	#evaluate final
	return evaluatePart2(equation)


def parseEquation(equation):
	parensPairs = parseParens(equation)

	#flatten the equation
	while parensPairs:
		pair = [x for x in parensPairs if x[2] == max(x[2] for x in parensPairs)][0]
		#evaluate 1 subexpression in innermost layer
		subResult = evaluate(equation[pair[0]:pair[1]+1])
		equation = equation[0:pair[0]] + [str(subResult)] + equation[pair[1]+1:]

		parensPairs = parseParens(equation)

	#evaluate final
	return evaluate(equation)

def part1():
	data = readInput()

	outerSum = 0
	for equation in data:
		print(equation)
		result = parseEquation(equation)
		print(result)
		outerSum += result

		#input('wait')
	print(outerSum)		

def part2():
	data = readInput()

	outerSum = 0
	for equation in data:
		print(equation)
		result = parseEquationPart2(equation)
		print(result)
		outerSum += result

		#input('wait')
	print(outerSum)		

if __name__ == '__main__':
	#part1()
	part2()