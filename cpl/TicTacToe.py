import random
from Board import Board

class TicTacToe(Board):    

  def __init__(self):
    super().__init__(3, 3, '-', '|', ['X', 'O'])
    self.available_moves = self.height * self.width    
    self.last_player = 1

  def calculateLegalMove(self):
  	if self.available_moves == 0:
  		print('Here')
  		return None
  	random_spaces = random.randint(1, self.available_moves)
  	print(random_spaces)
  	for i in range(self.height):
  		for j in range(self.width):
  			if self.board[i][j] == self.empty_space: 				
  				if random_spaces == 1:
  					print(i,j)
  					return (i,j)
  				else:
  					random_spaces -= 1  	  	

  def next_player(self):
  	self.last_player ^= 1
  	return self.last_player

  def makeRandomMove(self):
  	move = self.calculateLegalMove()
  	if move:
  		self.makeMove(move,self.next_player())
  		self.available_moves -= 1

  #def lastMoveWinning(self):
  #	(j,i) = self.last_move
  #	return (all(map(lambda l: l[i] == players[last_player], self.board)) or 
  #          all([space == players[last_player] for space in self.board[j]) or
  #          ((i == j and 
  

  def gameOver(self):
  	return (self.available_moves == 0 or   	
  	        self.checkHorizontalConnection(self.last_move, 3) or
  	        self.checkVerticalConnection(self.last_move, 3) or
  	        self.checkDiagnolConnection(self.last_move, 3) )

  def simulateGame(self):
  	for i in range(4):
  		self.makeRandomMove()
  		self.printBoard() 
  		self.printGameState(False)
  	over = self.gameOver()
  	while not over:
  		self.makeRandomMove()
  		self.printBoard()
  		self.printGameState(False)
  		over = self.gameOver()
  	self.printBoard()
  	self.printGameState(True)

  	



  #def calculateGameOver(self):
  #	for i in self.board


  #def simulate(self):



  



  