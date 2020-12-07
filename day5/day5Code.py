import sys

def readInput():
	with open('day5input.txt', 'r') as f:
		data = f.read().splitlines()
	return data

def part1():
	data = readInput()

	seatIDs = []
	for x in data:
		rowSeq = x[0:7]
		colSeq = x[7:]

		rows = range(0,128)
		cols = range(0,8)

		for y in rowSeq:
			if y == 'F':
				#take front half of rows
				c = len(rows)
				rows = rows[0:c/2]
			else:
				#take back half of rows
				c = len(rows)
				rows = rows[c/2:]

		for z in colSeq:
			if z == 'L':
				#take the lower half
				d = len(cols)
				cols = cols[0:d/2]
			else:
				#take upper half
				d = len(cols)
				cols = cols[d/2:]

		print(rows)
		print(cols)

		print('This is the seat row {} and column {}'.format(rows[0], cols[0]))
		seatID = rows[0] * 8 + cols[0]
		seatIDs.append(seatID)

	print('This is the highest seat ID: {}'.format(max(seatIDs)))

	return seatIDs


def part2(seatIDs):
	#find your seat ID
	#build exhaustive list of seat IDs, and compare the sets

	rows = range(0,128)
	cols = range(0,8)

	allSeatIDs = []
	for row in rows:
		for col in cols:
			seatID = row * 8 + col
			allSeatIDs.append(seatID)

	candidateSeats = set(allSeatIDs) - set(seatIDs)
	print(candidateSeats)

	for candidate in list(candidateSeats):
		#the seats with IDs -1 and +1 were in the actual manifest
		if candidate-1 in seatIDs and candidate+1 in seatIDs:
			print('This is your seat: {}'.format(candidate))

if __name__ == "__main__":
	seatIDs = part1()

	part2(seatIDs)