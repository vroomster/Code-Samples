import random

class ConnectFourBoard(Board):    

  def __init__(self):
    super().__init__(6, 6, '-', '|', ['X', 'O'])    
    self.available_moves = board_width
    self.last_player = 1

  def calculateLegalMove(self):
  	if self.available_moves == 0:
  		return None
  	random_spaces = random.randint(0, self.available_moves)
  	for j in range(self.width):
  		if board[j][0] == self.empty_space:          
  			if random_spaces == 0:
  				return (board[j], reversed(board[j]).index(self.empty_space))
  			else:
  				random_spaces -= 1
    
  def next_player(self):
  	self.last_player ^= 1
  	return last_player

  def makeRandomMove(self):
  	(j,i) = calculateLegalMove()
  	if move:
  		self.makeMove((j,i),self.next_player())
      if i == 0:
        self.available_moves -= 1



  def simulateGame(self):
    over = self.gameOver()
    self.makeRandomMove()
    while not over:
      self.makeRandomMove()
      self.printBoard()
      self.printGameState(False)
    self.printBoard()
    self.printGameState(True)






  #def calculateGameOver(self):
  #	for i in self.board


  #def simulate(self):



  



  