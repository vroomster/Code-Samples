# Author: Varun Bandi
# Date: 1/21/2012
# Usage: python datacenter_cooling.py <input file name> <output file name>
# Purpose: Programming puzzle -- See problem Text
# Solution: Modified Depth first search where we add up all paths found
#           We also need to add certain tricks to eliminate searching long paths
#           that cannot possibly cover all the rooms. Examples of these include:
#           1) Connecting all rooms in a row or column and there are rows or columns 
#							 on either side that are unconnected
#           2) Disconnecting a room or rooms from possibly being covered. For the single
#							 room version, we can basically check if its incomving edges have already been
#               seen. For multiple rooms, how??
import sys

startroom_value = 2
endroom_value = 3
ownedroom_value = 0
notownedroom_value = 1

num_columns, num_rows = None, None
datacenter = []
datacenter_neighbors = []
owned_rooms = 0
start_room, end_room = None, None


def calc_neighbors((row,col)):
  neighbors = []  
  #print 'prev room :', prev_row, prev_col
  if row+1 < num_rows:  	
    neighbors.append((row+1,col, True))
  if row-1 >= 0:
    neighbors.append((row-1,col, True))
  if col+1 < num_columns:
    neighbors.append((row,col+1, True))
  if col-1 >= 0:
    neighbors.append((row,col-1, True))
  return neighbors

def check_center_bisection():
  if rowfreq[row] == num_columns-1 and row > 0 and row < num_rows:
    if any(freq < num_columns for freq in rowfreq[0:row]):
      if any(freq < num_columns for freq in rowfreq[row:num_rows]):              
        return 0
  if colfreq[col] == num_rows-1 and col > 0 and col < num_columns:
    if any(freq < num_rows for freq in colfreq[0:col]):
      if any(freq < num_rows for freq in colfreq[col:num_columns]):
      return 0          


#rowfreq[row] += 1
#colfreq[col] += 1  

#rowfreq[row] -= 1
#colfreq[col] -= 1


def count_paths(startroom, goalroom):  
  rowfreq = [0] * num_rows
  colfreq = [0] * num_columns  
    def search_from((row,col)):          
      if already_visited(datacenter[row][col][0]):
        return 0
      elif datacenter[row][col][0] == 1:
        return 0
      elif room == goalroom:
        return 1 if len(roomsvisited) == owned_rooms+1 else 0      
      else:                      
        sum_paths = 0
        datacenter[row][col][1] = True
        for i, next in enumerate(datacenter_neighbors[row][col]):
          if next[2]:
            datacenter_neighbors[row][col][i][2] = False            
            sum_paths += search_from((next[0], next[1]))
            datacenter_neighbors[row][col][i][2] = True
        pathcount = sum((search_from(next[0], next[1])) for next in datacenter_neighbors[row][col] if next[2])
        datacenter[row][col][1] = False
        return pathcount
  return search_from(startroom)


# Read plays, then problems from input file, then ouput for each problem the solution into output_file
#with open(sys.argv[1], 'r') as input_file:  
with open('large_datacenter.txt', 'r') as input_file:  
  split_line = input_file.readline().split(' ')
  num_columns, num_rows = int(split_line[0]), int(split_line[1])    
  for row, line in enumerate(input_file):            
    row_rooms = []
    row_neighbors = []    
    for col, room in enumerate(line.split()):      
      room_value = int(room)
      if room_value == 2:
        start_room = (row, col)
      elif room_value == 3:
        end_room = (row,col)
      elif room_value == 0:
        owned_rooms += 1
      row_rooms.append((room_value, False))
      row_neighbors.append(calc_neighbors(row,col))
    datacenter.append(row_rooms)     
    datacenter_neighbors.append(row_neighbors)



#output_file.write(num_columns, num_rows
#output_file.write(datacenter     
#output_file.write(start_room
#output_file.write(end_room
#output_file.write(owned_rooms

print count_paths(start_room, end_room)



