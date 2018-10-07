class PieceLocation:

	def __init__(self):
		
		self.letterCoordinate = 0
		self.numberCoordinate = 0
		self.piecesToChange = []
	
	def __init__(self, _letterCoordinate, _numberCoordinate):
	
		self.letterCoordinate = _letterCoordinate
		self.numberCoordinate = _numberCoordinate
		self.piecesToChange = []
	
	# end PieceLocation()