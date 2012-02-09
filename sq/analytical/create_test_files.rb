#File names tell you what the makeup of the data is

def createTestFile(num_files, file_name_append, num_transactions, amount1, amount2, card_present1, card_present2)
	num_files.times do
		time = Time.now.to_f
		file = File.new("#{time}#{file_name_append}.txt", 'w')
		num_transactions.times do |x|
			file.puts("{#{time}__#{x},  payment_id, #{amount1}, #{card_present1}, created_at}")
	  	file.puts("{#{time}__#{num_transactions + x}, payment_id, #{amount2}, #{card_present2}, created_at}")
		end
		file.close
	end
end
