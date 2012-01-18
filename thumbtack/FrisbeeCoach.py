from operator import itemgetter
from decimal import *

max_success_rates = {}

def writeOutput((plays_success_rate, plays_freq)):
  play_names=[]
  for index, freq in enumerate(plays_freq):
    play_name, play_gain, play_success_rate = sorted_plays[index]
    for i in range(freq):
      play_names.append(play_name)
  play_sequence = '-'.join(play_names)
  output_file.write("%.2f%% %s\n" % (plays_success_rate*100, play_sequence))

def calcBestPlays(goal_distance, goal_depth):
  #print 'Call to method: ', (goal_distance, goal_depth)
  if goal_distance in max_success_rates:
    #print 'Globals helped: ', goal_distance, max_success_rates[goal_distance]
    return max_success_rates[goal_distance]
  plays_success_rate = 0.0
  for index, (play, play_gain, success_rate) in enumerate(sorted_plays):  	
    if play_gain > (goal_distance + goal_depth):
      continue
    elif (play_gain >= goal_distance and play_gain <= (goal_distance + goal_depth) and 
          max_success_plays[0] < success_rate):
      plays_success_rate = success_rate
      plays_freq = [0]*len(plays)      
      plays_freq[index] += 1
      #print 'Current max play that reaches goal: ', goal_distance, plays_success_rate, plays_freq
    else:
      (remaining_plays_success_rate, remaining_plays_freq) = calcBestPlays(goal_distance - play_gain, goal_depth)
      #print 'Return from recursive method: ', remaining_plays_success_rate, remaining_plays_freq
      if plays_success_rate < success_rate * remaining_plays_success_rate:                  
        plays_freq = list(remaining_plays_freq)
        plays_freq[index] += 1
        plays_success_rate = success_rate * remaining_plays_success_rate        
        #print 'Current max play that did not reach goal first: ', plays_success_rate, plays_freq
  max_success_rates[goal_distance] = plays_success_rate, plays_freq
  #print 'Saved to globals: ', goal_distance, max_success_rates[goal_distance]
  return plays_success_rate, plays_freq


with open('input.txt', 'r') as input_file:
  with open('output.txt', 'w') as output_file:
    for line in input_file:
      if line.startswith('Play:'):
        play = line.split(' ')
        plays.append( (play[1], int(play[2]), (100 - float(play[3]))/100) )
        sorted_plays = sorted(plays, key=itemgetter(1), reverse=True)
      else:
        field = line.split(' ')
        writeOutput( calcBestPlays(int(field[0]), int(field[1]) ))
    
   

#plays = [ ('ShortLeft', 1, .98), ('ShortRight', 2, .97), ('MidRange', 18, .8), ('LongBomb', 36, .64) ]
#sorted_plays = sorted(plays, key=itemgetter(1), reverse=True)







#print sorted_plays

#print calcBestPlaySeries(	3, 5)

#print calcBestPlaySeries(20, 5)
 
#print calcBestPlaySeries(	34, 10)

#print calcBestPlaySeries(	75, 5)