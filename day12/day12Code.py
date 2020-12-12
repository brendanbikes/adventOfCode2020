from math import sin, cos, radians, sqrt, atan2, degrees
from numpy import arctan

def readInput():
	with open('day12input.txt','r') as f:
		return f.read().splitlines()


def part1():
	data = readInput()

	position = (0,0)
	direction = 0 #initial direction angle in degrees
	totalDistanceTraveled=0

	for instruction in data:

		code = instruction[0]
		number = int(instruction[1:])

		if code == "F":
			#move forward
			dX = number * cos(radians(direction))
			dY = number * sin(radians(direction))
			newPosition = (position[0] + dX, position[1] + dY)
			newDirection = direction
			totalDistanceTraveled += dX + dY
		
		elif code == 'N':
			#move north
			newPosition = (position[0], position[1] + number)
			newDirection = direction
			totalDistanceTraveled += number

		elif code == 'S':
			#move south
			newPosition = (position[0], position[1] - number)
			newDirection = direction
			totalDistanceTraveled += number

		elif code == 'E':
			#move east
			newPosition = (position[0] + number, position[1])
			newDirection = direction
			totalDistanceTraveled += number

		elif code == 'W':
			#move west
			newPosition = (position[0] - number, position[1])
			newDirection = direction
			totalDistanceTraveled += number
		
		elif code == 'L':
			newPosition = position
			newDirection = direction + number

		elif code == 'R':
			newPosition = position
			newDirection = direction - number

		#update position and direction
		position = newPosition
		direction = newDirection

	print('This is the Manhattan Distance: {}'.format(abs(position[0] + abs(position[1]))))


def part2():
	#waypoint
	data = readInput()

	shipPosition = (0,0)
	shipDirection = 0
	totalDistanceTraveled = 0

	waypointPosition = (10, 1) #1

	for instruction in data:
		print('\n')

		print(instruction)
		print('waypoint position {}'.format(waypointPosition))
		print('ship position {}'.format(shipPosition))
		code = instruction[0]
		number = int(instruction[1:])

		shipWaypointAngle = atan2(waypointPosition[1] - shipPosition[1], waypointPosition[0] - shipPosition[0])
		shipWaypointDistance = sqrt((waypointPosition[0] - shipPosition[0])**2 + (waypointPosition[1] - shipPosition[1])**2)

		print('ship waypoint angle {}'.format(degrees(shipWaypointAngle)))
		print('ship waypoint distance {}'.format(shipWaypointDistance))

		if code == "F":
			#move ship to waypoint n number of times
			dX = (waypointPosition[0] - shipPosition[0])
			dY = (waypointPosition[1] - shipPosition[1])

			shipPosition = (shipPosition[0] + number * dX, shipPosition[1] + number * dY)
			#totalDistanceTraveled += dX + dY

			#update waypoint position
			waypointPosition = (shipPosition[0] + dX, shipPosition[1] + dY)

		elif code == 'N':
			#move waypoint north
			waypointPosition = (waypointPosition[0], waypointPosition[1] + number)

		elif code == 'S':
			#move waypoint south
			waypointPosition = (waypointPosition[0], waypointPosition[1] - number)

		elif code == 'E':
			#move waypoint east
			waypointPosition = (waypointPosition[0] + number, waypointPosition[1])

		elif code == 'W':
			#move waypoint west
			waypointPosition = (waypointPosition[0] - number, waypointPosition[1])

		elif code == 'L':
			#move waypoint CCW around the ship
			shipWaypointAngle += radians(number)
			waypointPosition = (shipWaypointDistance * cos(shipWaypointAngle) + shipPosition[0], shipWaypointDistance * sin(shipWaypointAngle) + shipPosition[1])

		elif code == 'R':
			#move waypoint CW around the ship
			shipWaypointAngle -= radians(number)
			waypointPosition = (shipWaypointDistance * cos(shipWaypointAngle) + shipPosition[0], shipWaypointDistance * sin(shipWaypointAngle) + shipPosition[1])

		#round
		shipPosition = (round(shipPosition[0]), round(shipPosition[1]))
		waypointPosition = (round(waypointPosition[0]), round(waypointPosition[1]))


	print('This is the Manhattan Distance: {}'.format(abs(shipPosition[0]) + abs(shipPosition[1])))


if __name__ == "__main__":
	part1()
	part2()