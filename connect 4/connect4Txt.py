# Description: simulates a connect 4 game.

PLAYER_ONE="X"
COMPUTER="O"
PLAYER_TWO="O"
BLANK="_"
WIN_PLR_ONE="Player 1"
WIN_COMP="Computer"
WIN_PLR_TWO="Player 2"
DRAW="Draw"
LAST_THREE=3
NEXT_SPOT=1
NEXT_NEXT_SPOT=2
YES="y"
NO="n"

# makeBoard() takes in the width and height of the desired board                 
#                 
# Input:         height of the board, width of the board
# Output:        a 2D array of the height and width of the board
def makeBoard(width,height):
	#makes a list and then puts another list inside to make it 2D
	row = []
	for i in range(width):
	  row.append(BLANK)
	  board = []
	for i in range(height):
		board.append(row[:])
	return board

### checkVert() takes in the board and checks if the board has any vertical wins
#
#	input: player turn and the board
# 	output: says who won and true or false if the game is done
def checkVert(board,width,height,char):
	win=False
	#loops through the range of the width
	for col in range(width):
  		#loops through the height minus 3 elements because it takes the first element and next three elements after it 
  		for row in range(height-LAST_THREE):
  		#if the top element 		and the element under that one 			and element under the second one and ...
  		# 													is the players piece
  			if((board[row][col]==char and board[row+1][col]==char \
  				and board[row+NEXT_NEXT_SPOT][col]==char\
  			 	and board[row+LAST_THREE][col]==char)):
  				#win is set to true
  				win=True
  			#win cannot be set back to false to ensure it doesnt cancel out the win 
	return win

### checkDiag() takes in the board and checks if the board has any diagonal wins
#
#	input: player turn and the board
# 	output: says who won and true or false if the game is done
def checkDiag(board,width,height,char):
	win=False
	#loop is the same as checkVert() but cuts down the width too 
	for col in range(width-LAST_THREE):
  		for row in range(height-LAST_THREE):
  			#Takes the element and the next three elements that are down one and over one
  			if((board[row][col]==char and board[row+1][col+1]==char\
  			 and board[row+NEXT_NEXT_SPOT][col+NEXT_NEXT_SPOT]==char\
  			 and board[row+LAST_THREE][col+LAST_THREE]==char)):
  				win=True
	return win

### checkBackDiag() takes in the board and checks if the board has any diagonal wins
#
#	input: player turn and the board
# 	output: says who won and true or false if the game is done
def checkBackDiag(board,width,height,char):
	win=False
	#does check diagonal but backwards
	for col in range(width-LAST_THREE):
		for row in range(LAST_THREE,height):
			if((board[row][col]==char and board[row-1][col+1]==char \
				and board[row-NEXT_NEXT_SPOT][col+NEXT_NEXT_SPOT]==char \
				and board[row-LAST_THREE][col+LAST_THREE]==char)):
				win=True
	return win

### checkHori() takes in the board and checks if the board has any horizontal wins
#
#	input: player turn and the board
# 	output: says who won and true or false if the game is done
def checkHoriz(board,width,height,char):
	win=False
	#does the same thing as vert but horizontal. decreases the width range and takes in the current column and the three after that
	for col in range(width-LAST_THREE):
  		for row in range(height):
  			if((board[row][col]==char and board[row][col+1]==char \
  				and board[row][col+NEXT_NEXT_SPOT]==char \
  				and board[row][col+LAST_THREE]==char)):
  				win=True
	return win

### compTurn() takes in the board and makes the computer do its turn
#	gets a random number and pulls until it is at an available spot
#	input: the board
# 	output: the board
def compTurn(board,width,height):
	column=0
	#increases the column until theres an available spot
	while(checkCol(board,column)==False):
		column+=1
		#updates the board
	board=placeChar(board,column+1,COMPUTER,height,width)
	return board

### compTurn() takes in the board and checks if the spot is available
#	input: the board and desired spot
# 	output: true or false
def checkCol(board,column):
	available=False
	#checks if the first element of the column is blank and if its avaiable returs true
	if(board[0][column]==BLANK):
		available=True
	return available

### p1Turn() takes in the board and makes the player do their turn
#
#	input: the board
# 	output: The board
def p1Turn(board,width,height):
	win=False
	print("Player 1 what is your choice?")
	print("Enter a column to place your piece in (1 -",width,"):",end="")
	column=int(input())
	#while the spot isnt in range of the board or the spot isnt available
	while((column>width or column<1) or checkCol(board,column-1)==False):
		print("Invalid spot. Please select another")
		print("Enter a column to place your piece in ( 1 -",width,"):",end="")
		column=int(input())
	board=placeChar(board,column,PLAYER_ONE,height,width)
	return board

### checkWin() calls functions to check for vertical, diagonal, horizontal and backwards diagonal wins
#	input: the board,the player's character, height of the board ,and width
# 	output: true or false
def checkWin(board,width,height,char):
	win=False
	if(checkVert(board,width,height,char)==True):
		win=True
	elif(checkDiag(board,width,height,char)==True):
		win=True
	elif(checkHoriz(board,width,height,char)==True):
		win=True
	elif(checkBackDiag(board,width,height,char)==True):
		win=True
	return win

### placeChar() places the piece in the lowest spot
#
#	input: the board,the desired spot,the player's character , height of the board ,and width
#	output: the board
def placeChar(board,spot,char,height,width):
	row=height-1
	spot-=1
	#while the spot is occupied, increase the row by one 
	while(board[row][spot]==PLAYER_ONE \
		or board[row][spot]==PLAYER_TWO \
		or board[row][spot]==COMPUTER):
			row-=1
	board[row][spot]=char
	return board			

### p2Turn() takes in the board and makes the player do their turn
#
#	input: the board
# 	output: says who won and true or false if the game is done
def p2Turn(board,width,height):
	win=False
	#same as player 1
	print("Player 2 what is your choice?")
	print("Enter a column to place your piece in (1 -",width,"):",end="")
	column=int(input())
	while((column>width or column<1) or checkCol(board,column-1)==False):
		print("Invalid spot. Please select another")
		print("Enter a column to place your piece in ( 1 -",width,"):",end="")
		column=int(input())
	board=placeChar(board,column,PLAYER_TWO,height,width)
	return board

### PvP() calls player 1 and two funtions until the game is over
#	
#	input: board
#	output: true or false, depending on if the game is over or not
def PvP(board,width,height):
	winner=""
	p1Win=False
	while(winner==""):
		#loops while there is no winner
		printBoard(width,height,board)
		board=p1Turn(board,width,height)
		p1Win=checkWin(board,width,height,PLAYER_ONE)
		if(p1Win==True):
			winner=WIN_PLR_ONE
		elif(p1Win==False):
			printBoard(width,height,board)
			board=p2Turn(board,width,height)
			p2Win=checkWin(board,width,height,PLAYER_TWO)
			if(p2Win==True):
				winner=WIN_PLR_TWO
		if(checkDraw(board,width,height)==True):
			winner=DRAW
	return winner

### checkDraw() Checks the number of black spaces to see if its the max number of spaces
#	
#	input: board, width, height
#	output: true or false, depending on if the board is blank
def checkDraw(board,width,height):
	numBlank=0
	draw=False
	maxSpot=width*height
	for i in range(height):
	  for x in range(width):
	  	if(board[i][x]==BLANK):
	  		numBlank+=1
	if(numBlank==maxSpot):
		draw=True
	else:
		draw=False

### PvC() calls player 1 and computer functions until the game is over
#	
#	input: board
#	output: true or false, depending on if the game is over or not
def PvC(board,width,height):
	winner=""
	while(winner==""):
		printBoard(width,height,board)
		board=p1Turn(board,width,height)
		p1Win=checkWin(board,width,height,PLAYER_ONE)
		if(p1Win==True):
			winner="Player 1"
		if(p1Win==False):
			board=compTurn(board,width,height)
			compWin=checkWin(board,width,height,COMPUTER)
			if(compWin==True):
				winner=WIN_COMP
	return winner

### printBoard() prints out the board
#
#	input: the board
#	output: prints the board
def printBoard(width,height,board):
	for i in range(height):
	  for x in range(width):
	    print(board[i][x],end=" ")
	  print()

def main():
	playAgain="y"
	winGame=False
	board=[]
	playCom="n"
	print("Welcome to Connect 4!")
	#while play again is true
	while(playAgain=="y"):
		playAgain="n"
		width=int(input("Enter a width: "))
		height=int(input("Enter a height: "))
		while(width<5 and height<5):
			print("Invalid input. Please pick a new size")
			width=int(input("Enter a width: "))
			height=int(input("Enter a height: "))
		board=makeBoard(width,height)
		playCom=input("Play against the computer? (y/n): ")
    		#if pvp is true:
		if(playCom=="n"):
			winner=PvP(board,width,height)
		else:
			winner=PvC(board,width,height)
		printBoard(width,height,board)
		if(winner==DRAW):
			print("Draw!")
		else:
			print(winner,"wins!")
		playAgain=input("Would you like to play again? (y/n): ")
		while(playAgain!=NO or playAgain!=YES):
			print("invalid input")
			playAgain=input("Would you like to play again? (y/n): ")

main()