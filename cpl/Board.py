import sys

class Board(object):    

  def __init__(self, width, height, empty_space, space_seperator, players):
    self.board = [[empty_space]*height for x in range(width)]    
    self.empty_space = empty_space
    self.space_seperator = space_seperator
    self.width = width
    self.height = height    
    self.players = players    
    self.last_move = None

  def printBoard(self):
  	sys.stdout.write("BOARD:\n")
  	for i in range(self.height):
  		for j in range(self.width):
  			sys.stdout.write(self.space_seperator)
  			sys.stdout.write(self.board[j][i])
  		sys.stdout.write(self.space_seperator)
  		sys.stdout.write('\n')

  def makeMove(self, move, player_index):
  	(j,i) = move
  	self.board[j][i] = self.players[player_index]
  	print(self.players[player_index])
  	self.last_move = (j,i)  	
  	#self.made_moves += 1

  def checkHorizontalConnection(self, move, num):
    (j,i) = move
    count, temp_j = 0, j
    while temp_j > 0 and self.board[temp_j][i] == self.board[temp_j-1][i]:
    	count+=1    		
    	temp_j-=1
    temp_j = j
    while temp_j < self.width-1 and self.board[temp_j][i] == self.board[temp_j+1][i]:
    	count+=1
    	temp_j+=1
    return count == num

  def checkVerticalConnection(self, move, num):
    (j,i) = move
    count, temp_i = 0, i
    while temp_i > 0 and self.board[j][temp_i] == self.board[j][temp_i-1]:
    	count+=1    		
    	temp_i-=1
    temp_i = i
    while temp_i < self.height-1 and self.board[j][temp_i] == self.board[j][temp_i+1]:
    	count+=1
    	temp_i+=1
    return count == num-1

  def checkDiagnolConnection(self, move, num):
    (j,i) = move
    count, temp_i, temp_j = 0, i, j
    while (temp_i < self.height-1 and temp_j < self.width-1) and self.board[temp_j][temp_i] == self.board[temp_j+1][temp_i+1]:
      count+=1
      temp_i+=1
      temp_j+=1
    temp_i,temp_j = i,j
    while (temp_i > 0 and temp_j > 0) and self.board[temp_j][temp_i] == self.board[temp_j-1][temp_i-1]:
      count+=1    		
      temp_i-=1
      temp_j-=1
    return count == num-1
    count == 0
    temp_i,temp_j = i,j
    while (temp_i > 0 and temp_j < self.width-1) and self.board[temp_j][temp_i] == self.board[temp_j+1][temp_i-1]:
      count+=1    		
      temp_i+=1
      temp_j+=1
    temp_i,temp_j = i,j
    while (temp_i < self.height-1 and temp_j > 0) and self.board[temp_j][temp_i] == self.board[temp_j-1][temp_i+1]:
      count+=1    		
      temp_i-=1
      temp_j-=1
    return count == num-1

  def printGameState(self, over):
  	sys.stdout.write("GAMEOVER? " + str(over))
  	sys.stdout.write('\n')
  



