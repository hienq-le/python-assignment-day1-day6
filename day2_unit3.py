# Word order
import re
max_number_of_words = 0
list_of_words = []
tmp_list_of_words = []
nums_of_appearances_in_order = []
i = 0
j = 0
count_appearances = 0
tmp_word = None
tmp_max_number_of_words = input('Enter maximum number of words to enter: ')
try:
	max_number_of_words = int(tmp_max_number_of_words)
except Exception:
	print('Error: The maximum number of words to enter wasn\'t an integer!')
	exit()
if max_number_of_words < 2:
	print('Error: The maximum number of words to enter can\'t meet conditions to find repeated words!')
	exit()
while len(list_of_words) < max_number_of_words:
	tmp_word = input('Enter a word or a string: ')
# Program declines null
	try:
		if tmp_word == None or len(tmp_word) == 0:
			raise ValueError
	except ValueError:
		print('Null found!')
		continue
	tmp_list_of_words = tmp_word.split()
	for j in range(len(tmp_list_of_words)):
		list_of_words.append(tmp_list_of_words[j])
# Program raises an IndexError if out of bound
	try:
		if len(list_of_words) > max_number_of_words:
			raise IndexError
	except IndexError:
		print('Error: Out of bound!')
		exit()
# Set target word at index 0 of list of words
target_word = list_of_words[0]
# Search for appearance of target word in list of words, then remove at index 0, repeat until list of words is empty, and print out array of number of appearances
while len(list_of_words) > 0:
	new_string = ''.join([str(e) for e in list_of_words])
	count_appearances = len(re.findall(target_word, new_string))
	nums_of_appearances_in_order.append(count_appearances)
	list_of_words.pop(0)
print(nums_of_appearances_in_order)