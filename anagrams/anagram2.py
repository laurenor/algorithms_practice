word_list = ['act','cat','boy','yob','ybo','meow','woem']
all_words = [w.strip() for w in open('words.txt')]

# def most_anagrams(word_list):
# 	word_list_dict = {}

# 	# adds words with anagram count to word_list_dict
# 	for i in range(len(word_list)): # 0,1,2
# 		first_word = word_list[i] 
# 		if first_word not in word_list_dict:
# 			word_list_dict[first_word] = 1
# 		for k in range(i+1,len(word_list)):
# 			second_word = word_list[k] 
# 			if (len(first_word) == len(second_word)) and (''.join(sorted(first_word)) == ''.join(sorted(second_word))):
# 				word_list_dict[first_word] += 1

# 	# adds anagrams with highest values to list
	# highest_key = None
	# for key in word_list_dict:
	# 	if highest_key == None:
	# 		highest_key = key
	# 	else:
	# 		if word_list_dict[key] > word_list_dict[highest_key]:
	# 			highest_key = key
	# 		elif word_list_dict[key] == word_list_dict[highest_key]: # Compares the indeces of the anagrams with highest values.  
	# 			if word_list.index(key) < word_list.index(highest_key): # Lowest index is returned
	# 				highest_key = key
	# return highest_key

def most_anagrams(word_list):
	word_list_dict = {}
	for word in word_list:
		sorted_word = ''.join(sorted(word))
		first_word_index = word_list.index(word)
		if sorted_word not in word_list_dict:
			word_list_dict[sorted_word] = (1, first_word_index)
		else:
			# print "tuple amt: ", word_list_dict[sorted_word][0]
			original_index = word_list_dict[sorted_word][1]
			new_count = word_list_dict[sorted_word][0] + 1
			word_list_dict[sorted_word] = (new_count, original_index)
	print word_list_dict

	highest_key = None
	for key in word_list_dict: 
		current_value = word_list_dict[key][0]
		if highest_key == None:
			highest_key = key
			highest_value = word_list_dict[highest_key][0]
		else:
			if current_value > highest_value:
				highest_key = key
				highest_value = word_list_dict[highest_key][0]
			elif current_value == highest_value:
				if word_list_dict[key][1] < word_list_dict[highest_key][1]:
					highest_key = key
	return highest_key




print most_anagrams(word_list)
print most_anagrams(all_words)