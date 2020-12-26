from numpy import dot

def readInput():
	with open('day22Input.txt', 'r') as f:
		data = [[int(y) for y in x.splitlines()[1:]] for x in f.read().split('\n\n')]
	return data


def part1():
	player1, player2 = readInput()

	while len(player1) > 0 and len(player2) > 0:
		#take the top cards off
		player1card = player1[0]
		player2card = player2[0]

		player1=player1[1:]
		player2=player2[1:]
		
		if player1card > player2card:
			#give cards to player 1
			player1 += [player1card, player2card]
		else:
			#give cards to player 2
			player2 += [player2card, player1card]

	#a player has won the game
	print('Player {} has won the game with {} points'.format(1 if len(player1)>0 else 0, dot(range(len(player1),0,-1), player1) if len(player1)>0 else dot(range(len(player2),0,-1), player2)))

def part2():
	player1, player2 = readInput()

	winner, deck = recursiveCombat(player1, player2)

	print('Player {} has won the game with {} points'.format(winner, dot(range(len(deck),0,-1), deck)))

def recursiveCombat(player1, player2):
	#start new history for this level
	history = []

	while len(player1) > 0 and len(player2) > 0 and tuple([player1, player2]) not in history:
		#do the combat

		#save the game state
		history.append((player1, player2))
		
		#draw a card from both
		player1card = player1[0]
		player2card = player2[0]
		player1 = player1[1:]
		player2 = player2[1:]

		if len(player1) >= player1card and len(player2) >= player2card:
			#recur into a subgame with copies of the decks
			winner, deck = recursiveCombat(player1[:player1card], player2[:player2card])

			if winner == 1:
				#player 1 won the subgame
				player1 += [player1card, player2card]

			elif winner == 2:
				#player 2 won the subgame
				player2 += [player2card, player1card]
		else:
			#round winner has higher card
			if player1card > player2card:
				#give cards to player 1
				player1 += [player1card, player2card]
				winner = 1
			else:
				#give cards to player 2
				player2 += [player2card, player1card]
				winner = 2

	#either hit a loop, or game is over
	if tuple([player1, player2]) in history:
		#immediately end the game in a win for player 1
		winner = 1
		return winner, player1

	if len(player1)>0:
		#player1 won the game
		winner = 1
		return winner, player1

	else:
		#player 2 won the game
		winner = 2
		return winner, player2

			
if __name__ == '__main__':
	part1()
	part2()