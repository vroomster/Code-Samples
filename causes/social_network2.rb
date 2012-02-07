require 'text'
require 'benchmark'

@max_str_len = 50
@total_words = 0

def get_word_list(file_name)
  file = File.new(file_name, 'r')
  str_lens = Array.new(@max_str_len) {Array.new}
  while (line = file.gets)    
    curr_word = line.rstrip	 
    str_lens[curr_word.length] << curr_word    
  end
  return str_lens 
end


def calc_social_network(main_word, strings_by_len)
  string_queue = [main_word]
  network_size = 0
  while not string_queue.empty?
    network_size += number_friends(string_queue.pop, strings_by_len, string_queue)
    p network_size
  end
  return network_size
end

def number_friends(curr_word, strings_by_len, string_queue)
  count = 0
  (curr_word.length-1..curr_word.length+1).each do |length|
    strings_by_len[length].each_with_index do |word, index| 
      if check_levenshtein_threshold(curr_word, word, 1)
        string_queue << strings_by_len[length].delete_at(index)
        count += 1
      end
    end 
  end
  return count
end

def check_levenshtein_threshold(str1, str2, threshold)
  return Text::Levenshtein.distance(str1, str2) == threshold
end


time = Benchmark.realtime do
p  calc_social_network('causes', get_word_list('word.list'))
end

puts "Time Elapsed #{time}"
















