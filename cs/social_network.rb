require 'text'
require 'benchmark'

@max_str_len = 50
#main_word = 'causes'

#Returns levenshtein distance with assumption that matrix distance has prefix_len
#rows of calculated values already
def levenshtein_distance(str1, str2, prefix_len, dist)
  for j in (1..str2.length) do 
    for i in (prefix_len+1..str1.length) do
      if (str1[i-1]  == str2[j-1])
        dist[i][j] = dist[i-1][j-1]
      else
        dist[i][j] = [dist[i-1][j]+1, dist[i-1][j-1]+1, dist[i][j-1]+1].min
      end
    end      
  end
  return dist[str1.length][str2.length]
end

#Returns the length of the common prefix substring that str1 and str2 start with
def common_prefix_len(str1, str2)
  min_len = [str1.length, str2.length].min
  (0..min_len).each { |i| if str1[i] != str2[i] then return i end }
  return smaller_str_len
end

#Calculates the social network for the main_word by calculating distances to 
#all words in the file, then inputting the counts into a bucket sort
#if words are sorted, we see big performance improvement
def sort_by_distances(main_word, file_name)
  strings_by_distance = Array.new(@max_str_len) {Array.new}
  file = File.new(file_name, 'r')
  prev_word = ""
  dist = Array.new(@max_str_len+1) {Array.new(main_word.length+1)}
  (0..@max_str_len).each { |i| dist[i][0] = i }
  (0..main_word.length).each { |j| dist[0][j] = j }
  while (line = file.gets)    
    curr_word = line.rstrip  
    prefix_len = common_prefix_len(curr_word, prev_word)  
    distance = levenshtein_distance(curr_word, main_word, prefix_len, dist) 
    strings_by_distance[distance] << curr_word  
    prev_word = curr_word
  end
  return strings_by_distance
end

def calc_all_distances2(main_word, file_name)
  distances = Array.new(50,0)
  file = File.new(file_name, 'r')
  while (line = file.gets)            
    distance = Text::Levenshtein.distance(line.rstrip, main_word) 
    distances[distance] += 1    
  end
  return distances
end

def calc_all_distances3(main_word, file_name)
  distances = Array.new(50,0)
  file = File.new(file_name, 'r')
  while (line = file.gets)            
    line
  end
  return distances
end

def trim_word_list(strings_by_distance)
  #(1..@max_str_len-2).each do |i|
  (0..0).each do |i|
    words = Array.new
    puts "Looking at indices #{i} and #{i+1}"
    strings_by_distance[i].each do |word1|
      strings_by_distance[i+1].each_with_index do |word2, index|
        if Text::Levenshtein.distance(word1, word2) == 1
          words << word2
          strings_by_distance[i+1].delete_at(index)
        end
      end
    end
    strings_by_distance[i+1] = end
  words
end

def trim_word_list2(strings_by_distance)
  (1..@max_str_len-2).each do |i|
    (i..@max_str_len-1).each do |j|
      words = Array.new
      puts "Looking at indices #{i} and #{j}"
      puts "Length at distance j: #{strings_by_distance[j].length}"
      strings_by_distance[j].each_with_index do |word2, index|
        strings_by_distance[i].each do |word1|      
          if Text::Levenshtein.distance(word1, word2) == j-i
            words << word2
            break
          end
        end
      end
      strings_by_distance[j] = words
      puts "Length at distance j: #{strings_by_distance[j].length}"
    end    
  end
end

#Calculates the network size by summing number words found at each distance
# until first empty bucket is reached
def get_network_size(distances)  
  sum = 0
  distances.each do |distance|
    if distance == 0
      break
    end
    sum += distance
  end
  return sum
end

#puts 'total network size: ', sum
#p lev_distances
#p dist

time = Benchmark.realtime do
  d = sort_by_distances('causes', 'word.list')
  #d.each_with_index { |words, i| puts "Index #{i}, length #{words.length}" }     
  #puts d[0]
  #puts 'Finished with index of 0'
  #puts d[1]
  puts "Length of array at 1 before is #{d[1].length}" 
  puts "Length of array at 2 before is #{d[2].length}" 
  #puts "Length of array at 3 before is #{d[3].length}"
  trim_word_list2(d)
  puts "Length of array at 1 after is #{d[1].length}"
  puts "Length of array at 2 after is #{d[2].length}"
  #puts "Length of array at 3 after is #{d[3].length}"
  puts d[2]  
end

puts "Time Elapsed #{time}"






