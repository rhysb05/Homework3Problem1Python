from GameBoard import GameBoard

myBoard = GameBoard()

myBoard.setcoordinate("B", 0, 0)
myBoard.setcoordinate("W", 0, 1)
myBoard.setcoordinate("W", 0, 2)
myBoard.setcoordinate("B", 7, 7)
myBoard.setcoordinate("W", 6, 7)
myBoard.setcoordinate("W", 5, 7)
myBoard.setcoordinate("B", 2, 0)
myBoard.setcoordinate("W", 3, 0)
myBoard.setcoordinate("W", 4, 0)
myBoard.setcoordinate("B", 3, 7)
myBoard.setcoordinate("W", 3, 6)
myBoard.setcoordinate("W", 3, 5)




myBoard.makepiecelist()
myBoard.makemovelist()



myBoard.printgrid()




print("Just here for breakpoint.")

