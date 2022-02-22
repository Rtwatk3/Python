# Author:  Ryan Watkins
SOLVE_PLAY=["s","p"]
YES_NO=["y","n"]
ONE_NINE=[1,2,3,4,5,6,7,8,9]
PLAY_CHOICES=["p","s","u","q"]
MAX_RANGE_VERT=9
MAX_RANGE_HORI=9

YN_PROMPT="Enter the filename of the Sudoku Puzzle: "
SOLVE_OR_PLAY="Play (p) or solve (s)? "
CORRECTNESS="Correctness checking? (y/n): "
P_S_U_Q="Play number (p), save (s), undo (u), quit (q): "

def doDeepCopy(boardToCopy):
	board=[]
	for x in range(len(boardToCopy)):
		board.append(list(boardToCopy[x]))
	for i in range(len(boardToCopy)):
		for x in range(len(boardToCopy[i])):
			numConvert=board[i][x]
			numConvert=int(numConvert)
			board[i][x]=numConvert
	return board

def boardFull(board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			if (board[row][col]==0):
				return False
	return True

def solve(board):
	if(boardFull(board)):
		return True
	else:
		#finds the first vacant spot
		cords=findVacant(board)
		vacX=cords[0]
		vacY=cords[1]
		possibleNumbers=getPossibleNum(vacX,vacY,board)
		for counter in range(len(possibleNumbers)):
			board[vacX][vacY]=possibleNumbers[counter]
			if(solve(board)):
				return True
		board[vacX][vacY]=0
		#since the board isnt full and there are no more possible numbers, set the current spot back to blank

def findVacant(board):
	cords=[]
	for x in range(len(board)):
		for y in range(len(board[x])):
			if(board[x][y]==0):	
				cords=[x,y]
				return cords

def getPossibleNum(row,col,board):
	possibleNumbers=ONE_NINE
	notPossibleNums=[]
	indexStartX=-1
	indexStartY=-1
	myNum=board[row][col]
	finalPossNum=[]
	#run through the row 
	for y in range(len(board[row])):
		#if the number is in the row
		if(not(board[row][y]==myNum)):
			notPossibleNums.append(int(board[row][y]))
	#run through the col
	for x in range(len(board)):
		#if the number is in the column
		if(not(board[x][col]==myNum)):
			notPossibleNums.append(int(board[x][col]))
	if(row<=2 and row>=0):
		indexStartRow=0
	elif(row<=5 and row>=3):
		indexStartRow=3
	else:
		indexStartRow=6

	if(col<=2 and col>=0):
		indexStartCol=0
	elif(col<=5 and col>=3):
		indexStartCol=3
	else:
		indexStartCol=6

	for finalRow in range(indexStartRow,indexStartRow+3):
		for finalCol in range(indexStartCol,indexStartCol+3):
			if(not(board[finalRow][finalCol]==myNum)):
				notPossibleNums.append(int(board[finalRow][finalCol]))
	for numCheck in range(len(possibleNumbers)):
		if(possibleNumbers[numCheck] not in notPossibleNums):
			finalPossNum.append(int(possibleNumbers[numCheck]))
	return finalPossNum

def validateInput(myChoices,prompt):
    choice=input(prompt)
    while(choice not in myChoices):
        print("Invalid input. Please enter a new choice")
        choice=input(prompt)
    return choice

def doMove(choice,board,undoList):
	if(choice=="p"):
		row=input("Enter a row number (1-9): ")
		col=input("Enter a column number (1-9): ")
		row=int(row)
		col=int(col)
		while(board[row][col]!=0):
			print("Invalid spot.")
			row=input("Enter a row number (1-9): ")
			col=input("Enter a column number (1-9): ")
		row+=1
		col+=1
		number=input("Please enter a number to put in cell ("+str(row-1)+" "+str(col-1)+"): ")
		number=int(number)
		while(number not in ONE_NINE):
			print("Invalid number.")
			number=input("Please enter a number from 1-9")
			number=int(number)

		numMoves=len(undoList)
		undoList[numMoves]=str(row)+","+str(col)+","+str(number)
	else:
		row=input("Enter a row number (1-9): ")
		col=input("Enter a column number (1-9): ")
		row=int(row)
		col=int(col)
		while(board[row][col]!=0):
			print("Invalid spot.")
			row=input("Enter a row number (1-9): ")
			col=input("Enter a column number (1-9): ")
		row+=1
		col+=1
		number=0
		while(validChoice(number,col,board,row)==False and number==0):
			number=input("Please enter a number to put in cell ("+str(row-1)+" "+str(col-1)+"): ")
			number=int(number)
			while(number not in ONE_NINE):
				print("Invalid number.")
				number=input("Please enter a number from 1-9")
				number=int(number)

		numMoves=len(undoList)
		undoList[numMoves]=str(row)+","+str(col)+","+str(number)
		return(undoList)

def validChoice(myNum,col,board,row):
	return checkNonet(row,col,board,myNum) and checkRow(row,board,myNum) and checkCol(col,board,myNum)

def changeBoard(plySvUnQu,deepCopy,undoList):
	moveNum=len(undoList)-1
	moveList=undoList[moveNum].split(",")
	row=moveList[0]
	col=moveList[1]
	number=moveList[2]
	row=int(row)
	col=int(col)
	number=int(number)
	deepCopy[row][col]=number
	return deepCopy

def doTurn(row,col,number,board):
	board[row][col]=number
	return board
    
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ") 
    print("  +-------+-------+-------+")
    for i in range(len(board)): 
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = board[i] 
        for j in range(len(boardRow)):
        	if boardRow[j] == 0:
        		boardRow[j] = "_"
        # fill in the row with the numbers from the board
	print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1, 
                boardRow[0], boardRow[1], boardRow[2], 
                boardRow[3], boardRow[4], boardRow[5], 
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")

def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

def readFile(fileName):
    starterBoard=open(fileName, "r")
    board=starterBoard.readlines()
    return board

def removeComma(text):
	myLine=""
	board=[]
	for row in range(len(text)):
		myLine=text[row]
		myLine=myLine.strip()
		myLine=myLine.split(",")
		board.append(myLine)

	for i in range(len(board)):
		for x in range(len(board[i])):
			numConvert=board[i][x]
			if(board[i][x]=="_"):
				board[i][x]=0
			numConvert=int(numConvert)
			board[i][x]=numConvert
	return(board)

def undo(moves,board):
	target=len(moves)-1
	del moves[target]
	return(moves)

def checkNonet(row,col,board,myNum):
	if(row<=2 and row>=0):
		indexStartRow=0
	elif(row<=5 and row>=3):
		indexStartRow=3
	else:
		indexStartRow=6

	if(col<=2 and col>=0):
		indexStartCol=0
	elif(col<=5 and col>=3):
		indexStartCol=3
	else:
		indexStartCol=6

	for finalRow in range(indexStartRow,indexStartRow+3):
		for finalCol in range(indexStartCol,indexStartCol+3):
			if(board[finalRow][finalCol]==myNum):
				print("Cannot place number.",myNum,"is already in this nonet.")
				return False

def checkRow(row,board,myNum):
	for y in range(len(board[row])):
		#if the number is in the row
		if(board[row][y]==myNum):
			print("Cannot place number.",myNum,"is already in this row.")
			return False

def checkCol(col,board,myNum):
	for x in range(len(board)):
		if(board[x][col]==myNum):
			print("Cannot place number.",myNum,"is already in this column.")
			return False

def main():
    filepath=input(YN_PROMPT)
    commaBoard=readFile("puzzles/"+filepath)
    board=removeComma(commaBoard)
    solved=doDeepCopy(board)
    deepCopy=doDeepCopy(board)
    prettyPrint(board)
    solve(solved)
    playSolve=validateInput(SOLVE_PLAY,SOLVE_OR_PLAY)
    if(playSolve==SOLVE_PLAY[0]):
    	print("Here is the solved puzzle.")
		prettyPrint(solved)
	else:
		correctPlay=validateInput(YES_NO,CORRECTNESS)
		print()
		quit=False
		undoList={}
		while(board!=solved and quit!=True):
			board=doDeepCopy(deepCopy)
			prettyPrint(board)
			plySvUnQu=validateInput(PLAY_CHOICES,P_S_U_Q)
			if(plySvUnQu==PLAY_CHOICES[3]):
				quit=True
			elif(plySvUnQu==PLAY_CHOICES[1]):
				savePuzzle(board,"puzzles/"+filepath)
			elif(plySvUnQu==PLAY_CHOICES[0]):
				if(correctPlay=="y"):
					undoList=doMove(correctPlay,deepCopy,undoList)
					deepCopy=changeBoard(plySvUnQu,deepCopy,undoList)
				else:
					undoList=doMove(plySvUnQu,deepCopy,undoList)
					deepCopy=changeBoard(plySvUnQu,deepCopy,undoList)


			else:
				deepCopy=changeBoard(plySvUnQu,deepCopy,undoList)
				undoList=undo(undoList,deepCopy)

main()