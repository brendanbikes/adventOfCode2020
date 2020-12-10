def readInput():
	with open('day9input.txt','r') as f:
		data = f.read().splitlines()
	return [int(x) for x in data]

def part1(data):

	i=25 #start at the 26th entry
	for number in data[25:]:
		nums = data[i-25:i]

		sums=[]
		for x in nums:
			remainder = nums[:]
			remainder.remove(x)

			sums += [y + x for y in remainder]

		if number not in sums:
			print('The current number is not valid. {}'.format(number))
			return number
		i+=1

def part2(data, targetNumber):
	for i in range(0,len(data)):
		#initialize
		sumPath=[]

		cumSum=data[i]
		sumPath.append(cumSum)

		while cumSum < targetNumber:
			i+=1
			cumSum+=data[i]
			sumPath.append(data[i])

		if cumSum == targetNumber and len(sumPath) > 1:
			print('Target sum has been reached, by summing these numbers: {}.'.format(sumPath))
			break
			#return cumSum, sumPath
		else:
			#overshot the target; try the next seed
			print('Sum overshot the target. Try the next seed.')

	print('This is the encryption weakness: {}'.format(sum([min(sumPath), max(sumPath)])))

if __name__ == "__main__":
	data = readInput()
	number = part1(data)
	part2(data, number)