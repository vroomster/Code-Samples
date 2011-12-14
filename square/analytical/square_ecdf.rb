=begin
Suppose you have multiple large files (on the order of 100GBs) containing tuples of the following form: 
{user_id, payment_id, payment_amount, is_card_present, created_at}. Write a program to compute the
 empirical cumulative distribution function of the card present ratio for users who processed less than
  $100, and for users who processed over $100.
 
The expected output should be of the form:
 
Users who processed less than $100
percentile    % cp
1             0
2             0
3             5
...           ...
100           100
 
and similarly for users who processed over $100.
=end
amount = 100
users_process_under_amount = Array.new(100, 0) #Hash['card_present_count' => 0, 'card_not_present_count' => 0])
users_process_over_amount = Array.new(100, 0)
under_counter, over_counter = 0.0, 0.0

# read from files (assume files are in same directory)
# change following code to read from file
Dir.glob('./test_input/*.txt') do |fileName| 
	#read from file
  file = File.new(fileName, 'r')
  while (line = file.gets)
	  values = line.scan(/\w+\.?\w+/)
	  user_id, payment_id, payment_amount, is_card_present, created_at = values[0], values[1], values[2], values[3], values[4]
	  if(payment_amount.to_f < 100)	 	    
	    if is_card_present == 'true'	    	
	  	  users_process_under_amount[under_counter%100] += 1	  	  
	  	end
	  	under_counter += 1 
	  else   #else if (payment > 100) if q was meant to exclude 100$ as an amount
	  	users_process_over_amount[over_counter%100] += 1 if is_card_present == 'true'
	  	over_counter += 1
	  end	  
  end
 file.close
end

under_sum, over_sum = 0.0, 0.0
puts 'Users who processed less than $#{amount}'
puts 'percentile        %cp'
100.times do |x|
	under_sum += users_process_under_amount[x]/under_counter * 100
	puts x+1, under_sum      
end

puts 'Users who processed more than $#{amount}'
puts 'percentile        %cp'
100.times do |x|
	over_sum += users_process_over_amount[x]/over_counter * 100
	puts x+1, over_sum
end

