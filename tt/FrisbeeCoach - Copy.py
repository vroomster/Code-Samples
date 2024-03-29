# Author: Varun Bandi
# Date: 1/15/2012
# Usage: python FrisbeeCoach.py <input
# Purpose: Programming puzzle -- See problem Text
# Solution: Recurive dynamic programming solution where we we save the most
#     optimal plays for any smaller distance computed. This way, extra work 
#     when the distance comes up in a later sub-problem, we don't recompute it.
from operator import itemgetter
from decimal import *
import sys

max_success_rates = {}
plays = []
sorted_plays = None

# Write the output in the format: 12.34% PlayName-PlayName-PlayName
def writeOutput((plays_success_rate, plays_freq)):
  play_names=[]
  for index, freq in enumerate(plays_freq):
    play_name, play_gain, play_success_rate = sorted_plays[index]
    for i in range(freq):
      play_names.append(play_name)
  play_sequence = '-'.join(play_names)
  output_file.write("%s%% %s\n" % ((plays_success_rate*100).quantize(Decimal('.01')), play_sequence))

# Calculate the most successful play or sequence of plays that ends in the goal area
def calcBestPlays(goal_distance, goal_depth):
  #Return best plays if already pre-computed in another sub-problem (or previous problem)
  if goal_distance in max_success_rates:
    return max_success_rates[goal_distance]    
  plays_success_rate, plays_freq = Decimal(0.0), [0]*len(plays)   
  for index, (play, play_gain, success_rate) in enumerate(sorted_plays):            
    # Play lands past goal area, try smaller (next) play
    if play_gain > (goal_distance + goal_depth):
      continue
    # Play lands perfectly in goal area, add it to play sequence
    elif (play_gain >= goal_distance and play_gain <= (goal_distance + goal_depth) and 
          plays_success_rate < success_rate):
      plays_success_rate = success_rate
      plays_freq = [0]*len(plays)      
      plays_freq[index] += 1
    # Play lands in field of play, calc success of remaining sequence of plays
    # then check against highest successful play or sequence found
    else:
      (remaining_plays_success_rate, remaining_plays_freq) = calcBestPlays(goal_distance - play_gain, goal_depth)
      if plays_success_rate < success_rate * remaining_plays_success_rate:                  
        plays_freq = list(remaining_plays_freq)
        plays_freq[index] += 1
        plays_success_rate = success_rate * remaining_plays_success_rate        
  # after all possible plays and sequences are explored, save the most successful to global array  
  max_success_rates[goal_distance] = plays_success_rate, plays_freq
  return plays_success_rate, plays_freq



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
    
   

#plays = [ ('ShortLeft', 1, .98), ('ShortRight', 2, .97), ('MidRange', 18, .8), ('LongBomb', 36, .64) ]
#sorted_plays = sorted(plays, key=itemgetter(1), reverse=True)







#print sorted_plays

#print calcBestPlaySeries(  3, 5)

#print calcBestPlaySeries(20, 5)
 
#print calcBestPlaySeries(  34, 10)

#print calcBestPlaySeries(  75, 5)