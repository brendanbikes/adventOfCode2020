import sys

def readInput():
	with open('day8input.txt', 'r') as f:
		data = f.read().splitlines()
	return [x.split(' ') for x in data]

def part1():
	data = readInput()

	executedIndices, accumulatorValues = iterate(0, [], data, [])
	print('The program did not complete, but reached {} successfully completed code lines before looping.'.format(len(executedIndices)))

	#print('The program terminated by attempting to access a command outside of the available range, at index {}. {}'.format(index, e))
	#print('This is the value of the accumulator after successful program completion: {}'.format(accumulatorValues[-1]))
	#print(accumulatorValues)

	#print('This is how many commands that successfully ran before loop was detected: {}'.format(len(executedIndices)))
	print('This is the value of the accumulator: {}'.format(accumulatorValues[-1]))
	#print('Did the program complete? {}'.format(didComplete))

def part2():
	data = readInput()

	i=0
	for row in data:
		code, value = row
		
		#make a fresh copy of the code
		dataFresh=[x for x in data]
		
		if code == 'nop' and int(value) != 0:
		 	#this is a valid nop to try flipping
		 	dataFresh[i] = ['jmp', value]
		 	executedIndices, accumulatorValues = iterate(0, [], dataFresh, [])

		elif code == 'jmp':
		 	#this is a valid jmp to try flipping
		 	dataFresh[i] = ['nop', value]
		 	executedIndices, accumulatorValues = iterate(0, [], dataFresh, [])
		i+=1

def iterate(index=0, accumulatorValues=[], data=None, executedIndices=[]):
	code, value = data[index]

	while index not in executedIndices:
		executedIndices.append(index)
		if code == 'nop':
			#no operation, proceed to next command
			index+=1
			if len(accumulatorValues)==0:
				accumulatorValues.append(0)
			else:
				accumulatorValues.append(accumulatorValues[-1])
		elif code =='acc':
			#change the accumulator value
			index+=1
			if len(accumulatorValues)==0:
				accumulatorValues.append(int(value))
			else:
				accumulatorValues.append(accumulatorValues[-1]+int(value))
		else:
			#jump to a new command
			index+=int(value)
			if len(accumulatorValues)==0:
				accumulatorValues.append(0)
			else:
				accumulatorValues.append(accumulatorValues[-1])

		if index == len(data)-1:
			#return current values -- program will complete successfully by running the last code line
			print('Program completed successfully: next command would be at index {}, the line after the last'.format(index))
			print('This is the accumulator value: {}'.format(accumulatorValues[-1]))
			print(accumulatorValues)
			print(executedIndices)
			break

		#call next iteration
		iterate(index, accumulatorValues, data, executedIndices)

	#print('Loop was detected; {} code lines were executed before loop.'.format(len(executedIndices)))

	return executedIndices, accumulatorValues

if __name__ == "__main__":
	#part1()
	part2()