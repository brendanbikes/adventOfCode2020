import sys

def readInput():
	with open('day25Input.txt', 'r') as f:
		return [int(x) for x in f.read().splitlines()]

def part1():
	cardPublicKey, doorPublicKey = readInput()

	#determine the loop sizes

	cardKey, cardLoops = iterate(cardPublicKey)
	doorKey, doorLoops = iterate(doorPublicKey)
		
	encryptionKey = encrypt(cardLoops, doorPublicKey)
	print(encryptionKey)

def iterate(publicKey, key=1, subjectNumber=7, divisor=20201227):
	loops=0
	while key != publicKey:
		loops+=1
		key *= subjectNumber
		key = key % divisor
	return key, loops

def encrypt(loops, subjectNumber, key=1, divisor=20201227):
	for i in range(0, loops):
		key *= subjectNumber
		key = key % divisor
	return key

if __name__ == '__main__':
	part1()