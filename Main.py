from GameBoard import GameBoard

myBoard = GameBoard()

# Set a variable that will control if the game has ended or not
winCondition = -1

myBoard.setcoordinate("B", 3, 3)
myBoard.setcoordinate("B", 4, 4)
myBoard.setcoordinate("W", 3, 4)
myBoard.setcoordinate("W", 4, 3)

# Make the initial piece and move list for the game
myBoard.makepiecelist()
myBoard.makemovelist()

print("Welcome to Othello!!\n\n We will now explain how the game is played.")
print("Othello is a strategy board game played between 2 players.")
print("Each player gets 32 discs and black always starts the game.")
print("Then the game alternates between white and black until:\n")
print("\t*one player can not make a valid move to outlfank the opponent")
print("\t*both players have no valid moves.")
print("\nWhen a player has no valid moves, they will pass their turn and the " +
      "opponent continues.")
print("A player cannot voluntarily forfeit their turn.")
print("When both players can not make a valid move, the game ends.")

while winCondition == -1:
	
	myBoard.printgrid()
	
	if len(myBoard.eligibleWhiteMoves) != 0:
		
		print("It is now the white player's turn")
		myBoard.printWhiteMoveList()
	
	# end if there are available moves
	
	# Update piece list and move list for the next player
	myBoard.makepiecelist()
	myBoard.makemovelist()
	
	if len(myBoard.eligibleBlackMoves) != 0:
		
		print("It is now the black player's turn")
		myBoard.printBlackMovesList()
	
	# end if there are available moves
	
	# Check to see if the win condition has been met
	myBoard.makepiecelist()
	myBoard.makemovelist()
	
	if len(myBoard.eligibleBlackMoves) == 0 and len(myBoard.eligibleWhiteMoves) == 0:
		
		# Set the win condition to 1 so that we can break out of the game loop
		print("There are not possible moves left. The game has eneded!!")
		print("Let's see who won!!")
		winCondition = 1
		
		blackPieces = len(myBoard.blackList)
		whitePieces = len(myBoard.whiteList)
		
		print("There are:", blackPieces, "black pieces on the board.")
		print("There are:", whitePieces, "white pieces on the board.")
		
		if whitePieces > blackPieces:
			
			print("The white player has won!!")
			
		# end if
		
		if blackPieces > whitePieces:
			
			print("The black player has won!!")
	
		# end if

	# end if the win condition has been met
	
# end while winCondition == -1




print("Just here for breakpoint.")

