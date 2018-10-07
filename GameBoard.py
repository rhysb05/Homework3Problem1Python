from PieceLocation import PieceLocation


class GameBoard:
	
	def __init__(self):
		
		self.LETTER_SIZE = 8
		self.NUMBER_SIZE = 8
		self.gameBoard = []
		self.eligibleBlackMoves = []
		self.eligibleWhiteMoves = []
		self.whiteList = []
		self.blackList = []
		
		# Initialize our 2D list
		for row in range(8):
			column = []
			for col in range(8):
				column.append("O")
			self.gameBoard.append(column)
	
	# end def __init__ GameBoard
	
	def getwhitelist(self):
		
		return self.whiteList
	
	# end getWhiteList()
	
	def getblacklist(self):
		
		return self.blackList
	
	# end getBlackList
	
	def geteligiblewhitemoves(self):
		
		return self.eligibleWhiteMoves
	
	# end getEligibleWhiteMoves
	
	def geteligibleblackmoves(self):
		
		return self.eligibleBlackMoves
	
	# end geteligibleblackmoves
	
	def setcoordinate(self, value, _letterCoordinate, _numberCoordinate):
		
		self.gameBoard[_numberCoordinate][_letterCoordinate] = value
	
	# end setcoordinate()
	
	def getcoordinate(self, _letterCoordinate, _numberCoordinate):
		
		return self.gameBoard[_numberCoordinate][_letterCoordinate]
	
	# end getcoordinate
	
	def printgrid(self):
		
		# Declare the variables needed to print out the grid headings
		columnheader = 'A'
		rownumber = 1
		
		# Print out a tab so that everything lines up
		print("\t", end="")
		
		# Use a for loop to print out the column labels.
		for i in range(8):
			print(columnheader, "\t", end="")
			# Increment character to print out next column heading
			columnheader = chr(ord(columnheader) + 1)
		
		# end for i in range(8)
		
		# Print a newline character
		print("")
		rownumber = 0
		
		for row in range(8):
			# Print the row at the beginning of each row
			print((rownumber + 1), "\t", end="")
			rownumber += 1
			
			for col in range(8):
				
				print(self.gameBoard[row][col], "\t", end="")
			
			# end for col in range(8)
			
			print("")
	
	# end for row in range(8)
	
	# end printgrid()
	
	def makepiecelist(self):
		
		self.whiteList.clear()
		self.blackList.clear()
		
		for row in range(8):
			for col in range(8):
				if self.gameBoard[row][col] == "B":
					
					_tempPiece = PieceLocation(col, row)
					self.blackList.append(_tempPiece)
				
				# end if piece is black
				
				if self.gameBoard[row][col] == "W":
					
					_tempPiece = PieceLocation(col, row)
					self.whiteList.append(_tempPiece)
			
			# end if piece is white
	
	# end for each element in grid
	
	# end makepiecelist()
	
	def makemovelist(self):
		
		# Clear the current move list in order to update the new one
		self.eligibleWhiteMoves.clear()
		self.eligibleBlackMoves.clear()
		
		# Create the lists that will hold the eligible white and black moves temporarily
		_tempEligibleBlackMoves = []
		_tempEligibleWhiteMoves = []
		
		# Go through whiteList and make list of all eligible moves.
		for whitePiece in self.whiteList:
			
			# Check each piece in blacklist against each piece in whitelist
			for blackPiece in self.blackList:
				
				# Determine if there is a piece to the right.
				if whitePiece.letterCoordinate < 7 and (whitePiece.letterCoordinate ==
				                                        (blackPiece.letterCoordinate - 1) and whitePiece.numberCoordinate == blackPiece.numberCoordinate):
					
					# Create a cursor variable to examine the next few pieces.
					cursor = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					
					firstPiece = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece to the right matches. Add that piece to the list of pieces to change.
					while cursor.letterCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate + 1,
					                                                         cursor.numberCoordinate) == "B":
						
						_tempPiece = PieceLocation(cursor.letterCoordinate + 1, cursor.numberCoordinate)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction.
						cursor.letterCoordinate += 1
					
					# end while next piece matches
					
					# Check to see if the space next ot the cursor is empty.
					if cursor.letterCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate + 1,
					                                                      cursor.numberCoordinate) == "O":
						
						# Create and place the PieceLocation object into the eligible move list
						_move = PieceLocation(cursor.letterCoordinate + 1, cursor.numberCoordinate)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleWhiteMoves.append(_move)
						
						self.eligibleWhiteMoves = _tempEligibleWhiteMoves
				
				# end if the space next to the cursor is empty
				
				# end if there is a piece to the right.
				
				# If there is a piece to the left
				if whitePiece.letterCoordinate > 0 and (whitePiece.letterCoordinate == (blackPiece.letterCoordinate + 1)
				                                        and blackPiece.numberCoordinate == whitePiece.numberCoordinate):
					
					#Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					
					firstPiece = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece to the left matches. Add that piece to the list of pieces to change
					while cursor.letterCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate - 1,
					                                                         cursor.numberCoordinate) == "B":
						
						_tempPiece = PieceLocation(cursor.letterCoordinate - 1, cursor.numberCoordinate)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction.
						cursor.letterCoordinate -= 1
					
					# end while pieces match
					
					# Check to see if the space next to the last piece is empty
					
					if cursor.letterCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate -1,
					                                                      cursor.numberCoordinate) == "O":
						
						# Create and place the PieceLocation object into the eligible move list
						_move = PieceLocation(cursor.letterCoordinate - 1, cursor.numberCoordinate)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleWhiteMoves.append(_move)
						
						self.eligibleWhiteMoves = _tempEligibleWhiteMoves
				
				# end if the space next to the last piece is empty
				
				# end if there is a piece to the left
				
				# If there is a piece below
				if whitePiece.numberCoordinate < 7 and (whitePiece.numberCoordinate == blackPiece.numberCoordinate - 1 and
				                                        whitePiece.letterCoordinate == blackPiece.letterCoordinate):
					
					#Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					
					firstPiece = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece below matches. Add that piece to the list of pieces to change.
					while cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                         cursor.numberCoordinate + 1) == "B":
						
						_tempPiece = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate + 1)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction
						cursor.numberCoordinate += 1
					
					# end while the piece below matches.
					
					# Check to see if the space below the blackpice is empty.
					if cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                      cursor.numberCoordinate +1) == "O":
						
						# Create and place the piece location object into the eligble moves list.
						_move = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate + 1)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleWhiteMoves.append(_move)
					
					self.eligibleWhiteMoves = _tempEligibleWhiteMoves
			
				# end if the space below is empty
			
				#end if there is a piece below
				
				# If there is a piece above
				if whitePiece.numberCoordinate > 0 and (whitePiece.numberCoordinate == (blackPiece.numberCoordinate + 1) and
				                                        whitePiece.letterCoordinate == blackPiece.letterCoordinate):
					
					# Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					
					firstPiece = PieceLocation(blackPiece.letterCoordinate, blackPiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece below matches. Add that piece to the list of pieces to change.
					while cursor.numberCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate,
					                                                         cursor.numberCoordinate - 1) == "B":
						_tempPiece = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate - 1)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction
						cursor.numberCoordinate -= 1
					
					# end while the piece above matches.
					
					# Check to see if the space below the blackpice is empty.
					if cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                      cursor.numberCoordinate - 1) == "O":
						# Create and place the piece location object into the eligble moves list.
						_move = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate - 1)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleWhiteMoves.append(_move)
					
					self.eligibleWhiteMoves = _tempEligibleWhiteMoves
				
					# end if the space above is empty
		
				# end if there is a piece above
	
			# end for blackpiece in self.blacklist
	
		# end for whitepiece in self.whitelist

		for blackPiece in self.blackList:
			
			for whitePiece in self.whiteList:
				
				# Determine if there is a piece to the right.
				if blackPiece.letterCoordinate < 7 and (blackPiece.letterCoordinate ==
				                                        (whitePiece.letterCoordinate - 1)
				                                        and blackPiece.numberCoordinate == whitePiece.numberCoordinate):
					
					# Create a cursor variable to examine the next few pieces.
					cursor = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					
					firstPiece = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece to the right matches. Add that piece to the list of pieces to change.
					while cursor.letterCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate + 1,
					                                                         cursor.numberCoordinate) == "W":
						_tempPiece = PieceLocation(cursor.letterCoordinate + 1, cursor.numberCoordinate)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction.
						cursor.letterCoordinate += 1
					
					# end while next piece matches
					
					# Check to see if the space next ot the cursor is empty.
					if cursor.letterCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate + 1,
					                                                      cursor.numberCoordinate) == "O":
						# Create and place the PieceLocation object into the eligible move list
						_move = PieceLocation(cursor.letterCoordinate + 1, cursor.numberCoordinate)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleBlackMoves.append(_move)
						
						self.eligibleBlackMoves = _tempEligibleBlackMoves
				
				# end if the space next to the cursor is empty
				
				# end if there is a piece to the right.
				
				# If there is a piece to the left
				if blackPiece.letterCoordinate > 0 and (blackPiece.letterCoordinate == (whitePiece.letterCoordinate + 1)
				                                        and whitePiece.numberCoordinate == blackPiece.numberCoordinate):
					
					# Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					
					firstPiece = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece to the left matches. Add that piece to the list of pieces to change
					while cursor.letterCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate - 1,
					                                                           cursor.numberCoordinate) == "W":
						
						_tempPiece = PieceLocation(cursor.letterCoordinate - 1, cursor.numberCoordinate)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction.
						cursor.letterCoordinate -= 1
					
					# end while pieces match
					
					# Check to see if the space next to the last piece is empty
					
					if cursor.letterCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate - 1,
					                                                      cursor.numberCoordinate) == "O":
						# Create and place the PieceLocation object into the eligible move list
						_move = PieceLocation(cursor.letterCoordinate - 1, cursor.numberCoordinate)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleBlackMoves.append(_move)
						
						self.eligibleBlackMoves = _tempEligibleBlackMoves
				
				# end if the space next to the last piece is empty
				
				# end if there is a piece to the left
				
				# If there is a piece below
				if blackPiece.numberCoordinate < 7 and (
						blackPiece.numberCoordinate == whitePiece.numberCoordinate - 1 and
						blackPiece.letterCoordinate == whitePiece.letterCoordinate):
					
					# Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					
					firstPiece = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece below matches. Add that piece to the list of pieces to change.
					while cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                         cursor.numberCoordinate + 1) == "W":
						_tempPiece = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate + 1)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction
						cursor.numberCoordinate += 1
					
					# end while the piece below matches.
					
					# Check to see if the space below the blackpice is empty.
					if cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                      cursor.numberCoordinate + 1) == "O":
						
						# Create and place the piece location object into the eligble moves list.
						_move = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate + 1)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleBlackMoves.append(_move)
					
					self.eligibleBlackMoves = _tempEligibleBlackMoves
				
				# end if the space below is empty
				
				# end if there is a piece below
				
				# If there is a piece above
				if blackPiece.numberCoordinate > 0 and (
						blackPiece.numberCoordinate == (whitePiece.numberCoordinate + 1) and
						blackPiece.letterCoordinate == whitePiece.letterCoordinate):
					
					# Create a cursor variable to examine the next few pieces
					cursor = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					
					firstPiece = PieceLocation(whitePiece.letterCoordinate, whitePiece.numberCoordinate)
					cursor.piecesToChange.append(firstPiece)
					
					# While the piece below matches. Add that piece to the list of pieces to change.
					while cursor.numberCoordinate > 0 and self.getcoordinate(cursor.letterCoordinate,
					                                                         cursor.numberCoordinate - 1) == "W":
						_tempPiece = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate - 1)
						cursor.piecesToChange.append(_tempPiece)
						
						# Move the cursor in the appropriate direction
						cursor.numberCoordinate -= 1
					
					# end while the piece above matches.
					
					# Check to see if the space below the blackpice is empty.
					if cursor.numberCoordinate < 7 and self.getcoordinate(cursor.letterCoordinate,
					                                                      cursor.numberCoordinate - 1) == "O":
						
						# Create and place the piece location object into the eligble moves list.
						_move = PieceLocation(cursor.letterCoordinate, cursor.numberCoordinate - 1)
						_move.piecesToChange = cursor.piecesToChange
						_tempEligibleBlackMoves.append(_move)
					
					self.eligibleBlackMoves = _tempEligibleBlackMoves
			
					# end if the space above is empty
		
				# end if there is a piece above
	
			# end for whitePiece in self.whiteList
	
		# end for blackPiece in self.blacklist
	
	# end make movelist()
	
	def switchlettercoordinate(self, _moveLetterCoordinate):
	
		switcher = {
			0: "A",
			1: "B",
			2: "C",
			3: "D",
			4: "E",
			5: "F",
			6: "G",
			7: "H"
		}
		
		_moveLetterCoordinate = switcher.get(_moveLetterCoordinate)
		
		return _moveLetterCoordinate
	
	# end switch letter coordinate

	def printWhiteMoveList(self):
		
		print("Possible moves for the white player")
		print("")
		
		counter = 0
		
		for _move in self.eligibleWhiteMoves:
			
			letterToPrint = ""
			
			