##day2code
import csv
import re

def readInput():
	with open('day2input.txt', 'r') as f:
		reader = csv.reader(f, delimiter = ' ')
		data = [x for x in reader]
	return data


def processPart1():
	data = readInput()

	validCount = 0
	for row in data:
		print(row)
		min, max = row[0].split('-')
		letter = row[1][0]
		password = row[2]
		matches = countNonOverlappingMatches(letter, password)
		if matches >= int(min) and matches <= int(max):
			print('Password {} is valid'.format(password))
			validCount+=1
		else:
			print('Password {} is invalid.'.format(password))

	print('There were {} valid passwords.'.format(validCount))

def countNonOverlappingMatches(pattern, string):
	return re.subn(pattern, '', string)[1] #only return the count


def processPart2():
	data = readInput()

	validCount=0
	for row in data:
		print(row)
		pos1, pos2 = row[0].split('-')
		letter = row[1][0]
		password = row[2]
		if bool(password[int(pos1)-1] == letter) ^ bool(password[int(pos2)-1] == letter):
			print('Password {} is valid.'.format(password))
			validCount+=1
		else:
			print('Password {} is invalid.'.format(password))

	print('Thwere were {} valid passwords.'.format(validCount))

if __name__ == "__main__":
	processPart2()