import random

print("\t#------------------Welcome to Tic-Tac-Toe------------------#")
player1 = str(input("Enter player1 name:"))
player2 = str(input("Enter player 2 name:"))

def printboard():
	"""Prints the gameboard in a matrix format"""
	for rows in range(3):
		for columns in range(3):
			print(gameboard[rows][columns]," ",end=" ")
		print("\n")

def TicTacToe():
	"""Initializes the game and calls choose method to set player symbols.
	Game continues till 9 moves(board is filled) or one of the player wins.
	PLayer must enter a number from (0-9) corresponding to the board positions
	Author:	MaVericKWareZ(Sarthak Mahapatra)
	"""
	move = 0
	turn = 0
	choose()
	for move in range(9):
		mover(move,turn)
		move += 1
		if check(turn,move):
			win(turn)
			break
		else:
			turn = (move%2)
	if flag == 0:
		print("Game is Drawn!!")

def player(turn):
	"""Returns the name of the player who is playing the turn"""
	if turn == 0:
		return str(player1)
	else:
		return str(player2)

def validMove(row,column):
	"""Checks whether the move entered is valid or not.
	If a move has already been played then it is invalid"""
	if gameboard[row][column] == '_':
		return True
	else:
		return False
def choose():
	"""A function which allows the players to choose their symbol from X or O"""
	x = random.randint(0,1)
	global player1Symbol 
	global player2Symbol 
	if x == 0:
		print(player1+" choose a symbol(X/O):")
		player1Symbol = input()
		if player1Symbol == 'X':
			player2Symbol = 'O'
		else:
			player2Symbol = 'X'
	else:
		print(player2+" choose a symbol(X/O):")
		player2Symbol = input()
		if player2Symbol == 'X':
			player1Symbol = 'O'
		else:
			player1Symbol = 'X'

def getSymbol(turn):
	"""Returns the symbol of the player who is playing the turn"""
	if player(turn) is player1:
		return player1Symbol
	else:
		return player2Symbol

def mover(move,turn):
	"""Function which accepts input from the user regarding the move and changes the gameboard accordingly"""
	setMove = getSymbol(turn) 
	print("Enter your move "+str(player(turn))+" (1-9):")
	tempMove = int(input())
	row = (tempMove-1)//3
	column = (tempMove-1)%3
	if validMove(row,column):
		gameboard[row][column] = setMove
		printboard()
	else:
		print('This is an invalid move.Please choose a move again')
		mover(move,turn)

def check(turn,move):
	"""Checks all victory conditons for the existing gameboard.
	Player can win in 3 ways:	1)Diagonally
								2)Row wise
								3)Column wise
	"""
	#check main-diagonal
	if (gameboard[0][0] == gameboard [1][1]) and (gameboard[1][1] == gameboard[2][2]) and (gameboard[0][0] != '_'):
		return True
	#check other diagonal
	elif (gameboard[0][2] == gameboard[1][1]) and (gameboard[1][1] == gameboard[2][0]) and (gameboard[0][2] != '_'):
		return True
	#check rows
	for rows in range(3):
		if (gameboard[rows][0] == gameboard[rows][1]) and (gameboard[rows][1] == gameboard[rows][2]) and (gameboard[rows][0] != '_'):	
			return True
	#check columns
	for columns in range(3):
		if (gameboard[0][columns] == gameboard[1][columns]) and (gameboard[1][columns] == gameboard[2][columns]) and (gameboard[0][columns] != '_'):
			return True
	return False

def win(turn):
	"""Declares the winner of the Game"""
	global flag 
	flag = 1
	print(player(turn)+" has won!!")

if __name__ == '__main__':
	gameboard = [['_','_','_'],['_','_','_'],['_','_','_']]
	player2Symbol = ' '
	player1Symbol = ' '
	flag = 0 
	TicTacToe()

	


