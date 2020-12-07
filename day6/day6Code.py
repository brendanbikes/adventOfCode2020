


def readInput():
	with open('day6input.txt', 'r') as f:
		data = f.read().split('\n\n')
	return data


def part1():
	data = readInput()

	total_count=0
	for group in data:
		people = group.split('\n')

		answers = set()
		for x in people:
			answers.update(list(x))
		total_count+=len(answers)

	print('This is the total number of yes answers among all groups, questions held to uniqueness within each group: {}'.format(total_count))


def part2():
	data = readInput()

	total_count=0
	for group in data:
		people = group.split('\n')

		answers = list()

		commonToAll = set(people[0]) #set to first element

		for x in people:
			commonToAll = commonToAll.intersection(x)

		total_count+=len(commonToAll)

	print('This is the total number of questions to which entire groups answered yes: {}'.format(total_count))


if __name__ == "__main__":
	part1()
	part2()
