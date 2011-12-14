#File names tell you what the makeup of the data is

def createTestFile(num_files, file_name_append, num_transactions, amount1, amount2, card_present1, card_present2)
	num_files.times do
		time = Time.now.to_f
		file = File.new("#{time}{file_name_append}.txt", 'w')
		num_transactions.times do |x|
			file.puts('{user_id, payment_id, #{amount1}, true, created_at}')
	  	file.puts('{user_id, payment_id, #{amount2}, false, created_at}')
		end
		file.close
	end
end
