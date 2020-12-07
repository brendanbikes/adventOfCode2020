import csv
import numpy as np


def read_input():
	with open('day1input.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		return np.array([int(x[0]) for x in reader])

def process(data):
	for x in data:
		summed = data + x
		for y in summed:
			if y == 2020:
				print('These two numbers summed to 2020.')
				print(x, y-x)
				print('This is their product.')
				print(x*(y-x))
				return

def process2(data):
	for x in data:
		for y in data:
			for z in data:
				if x + y + z == 2020:
					print('These three numbers summed to 2020.')
					print(x, y, z)
					print('This is their product.')
					print(x*y*z)
					return

if __name__ == "__main__":
	process(read_input())
	process2(read_input())