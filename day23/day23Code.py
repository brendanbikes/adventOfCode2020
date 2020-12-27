import sys
from collections import deque

def readInput():
	return [int(x) for x in list(str(368195742))] ## 368195742

def process1(data, rounds):
	k=0

	while k < rounds:
		#print('\nround {}'.format(k))
		currentCup = data[0]
		#do a round of moves
		#print('timepoint 1')
		#get index in array of currentCup
		currentIndex = 0
		#print('timepoint 2')

		#get 3 cups clockwise of current cup
		pickUpCups = data[1:4]

		#print('timepoint 3')

		#take the 3 cups out of the array
		data = [x for x in data if x not in pickUpCups]

		#print('timepoint 4')

		#find target for insertion
		z=currentCup-1 #starting search value

		while z not in data:
			z-=1 #decrement by 1

			if z < min(data):
				#set z to highest value
				z = max(data)

		#print('timepoint 5')

		#z is the value of the destination cup
		#insert pickUpCups into array, split at z
		zIndex = data.index(z)

		#print('timepoint 6')

		data = data[0:zIndex+1] + pickUpCups + data[zIndex+1:]
		#print('timepoint 7')
		#shuffle array backward by 1, so the next currentCup is still at index 0
		data.append(data[0])
		data = data[1:]
		#print('timepoint 8')

		k+=1

	return data

def process2(data, rounds):
	k = 0

	#put data into a dictionary
	d = {}
	for i, x in enumerate(data[:-1]):
		d[x] = data[i+1]

	#wrap the last value
	d[data[-1]] = data[0]

	#starting value
	currentCup = data[0]

	minimum = min(data)
	maximum = max(data)

	while k < rounds:

		cup1 = d.get(currentCup)
		cup2 = d.get(cup1)
		cup3 = d.get(cup2)

		cups = [cup1, cup2, cup3]

		#pop these cups out -- make currentCup linked to the cup that cup3 linked to
		d[currentCup] = d.get(cup3)

		#find target for insertion

		z=currentCup-1

		while z in cups or z < minimum:
			z-=1
			if z < minimum:
				z = maximum

		#do the insertion -- end of snip first
		d[cup3] = d.get(z)
		d[z] = cup1

		#update current cup 1 to the right
		currentCup = d.get(currentCup)

		#input('wait')
		k+=1

	return d


def part1():
	data = readInput()

	rounds = 100

	data = process(data, rounds)

	#find where 1 is
	index1 = data.index(1)

	#get result

	print(''.join(data[index1+1:] + data[0:index1]))


def part2():
	data = readInput()

	#add more data
	N = 1000000 #max number of cups
	#N = 200
	data = data + list(range(max(data)+1,N+1))

	rounds = 10000000
	#rounds = 1000
	data = process2(data, rounds)

	#print(data)
	#get results
	print(data.get(1))
	print(data.get(data.get(1)))

	print(data.get(1)*data.get(data.get(1)))


if __name__ == "__main__":
	#part1()
	part2()