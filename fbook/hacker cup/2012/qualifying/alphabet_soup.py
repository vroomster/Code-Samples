# Author: Varun Bandi
# Date: 1/20/2012
# Usage: python <script name>.py <input file name> <output file name>
# Purpose: Programming puzzle -- See problem Text
# Solution: Recurive dynamic programming solution where we we save the most
#     optimal plays for any smaller distance computed. This way, extra work 
#     when the distance comes up in a later sub-problem, we don't recompute it.


#Freq array representing the distinct letters in Hackercup: H,A,C,K,E,R,U,P
test_cases = []
letters = {'H': 0, 'A': 0, 'C': 0, 'K': 0, 'E': 0, 'R': 0, 'U': 0, 'P': 0 }

def returnCount(sentence):
  for letter in sentence:
    if letter in letters:
      letters[letter] += 1
  letters['C'] /= 2
  return min([count for count in letters.values()])



# Read plays, then problems from input file, then ouput for each problem the solution into output_file
with open(sys.argv[1], 'r') as input_file:
  with open(sys.argv[2], 'w') as output_file:
    for line in input_file:      
      split_line = line.split(' ')
      if line.startswith('Play:'):              
        plays.append( (split_line[1], int(split_line[2]), (100 - Decimal(split_line[3]))/100) )        
      else:
        sorted_plays = sorted(plays, key=itemgetter(1), reverse=True) if sorted_plays == None else sorted_plays        
        writeOutput( calcBestPlays(int(split_line[0]), int(split_line[1]) ))
    