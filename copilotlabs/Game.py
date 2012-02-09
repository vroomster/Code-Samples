class Game:    

  def __init__(self, name, board_width, board_height, empty_space, space_seperator):
    self.name = name
    self.board = Board(board_width, board_height, empty_space, space_seperator)    
    self.player1 = player1
    self.player2 = player2
    
  def printGameName(self):
    print self.name  	

  def makeRandomMove():