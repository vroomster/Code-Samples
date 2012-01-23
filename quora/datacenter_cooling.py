# Author: Varun Bandi
# Date: 1/21/2012
# Usage: python datacenter_cooling.py <input file name> <output file name>
# Purpose: Programming puzzle -- See problem Text
# Solution: Modified Depth first search where we add up all paths found
#     

startroom_value = 2
endroom_value = 3
ownedroom_value = 0
notownedroom_value = 1

num_columns, num_rows = None, None
datacenter = []
owned_rooms = 0
start_room, end_room = None, None


def neighbors((row,col)):
  neighbors = []
  if row+1 < num_rows:  	
    neighbors.append((row+1,col))
  if row-1 >= 0:
    neighbors.append((row-1,col))
  if col+1 < num_columns:  	
    neighbors.append((row,col+1))
  if col-1 >= 0:
    neighbors.append((row,col-1))
  return neighbors


def count_paths(startroom, goalroom):  
  def search_from(room, roomsvisited):
      if room in roomsvisited or datacenter[room[0]][room[1]] == 1:
          return 0
      elif room == goalroom:
      	  #print 'This should be equal at some point: ', len(roomsvisited), owned_rooms+1
          return 1 if len(roomsvisited) == owned_rooms+1 else 0
      else:
          roomsvisited.add(room)
          return sum(
              search_from(nextroom, roomsvisited.copy()) for nextroom in neighbors(room)
          )
  return search_from(startroom, set())


# Read plays, then problems from input file, then ouput for each problem the solution into output_file
#with open(sys.argv[1], 'r') as input_file:  
with open('small_datacenter.txt', 'r') as input_file:  
  split_line = input_file.readline().split(' ')
  num_columns, num_rows = int(split_line[0]), int(split_line[1])    
  for row, line in enumerate(input_file):            
    row_rooms = []
    for col, room in enumerate(line.split()):      
      if int(room) == 2:
        start_room = (row, col)
      elif int(room) == 3:
        end_room = (row,col)
      elif int(room) == 0:
        owned_rooms += 1
      row_rooms.append(int(room))
    datacenter.append(row_rooms)     



#print num_columns, num_rows
#print datacenter     
#print start_room
#print end_room
#print owned_rooms

print count_paths(start_room, end_room)


#writeOutput( calcBestPlays(int(split_line[0]), int(split_line[1]) ))
    