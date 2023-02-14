# Credit card validation
import re
credit_card_number = 0
credit_card_number_in_string_type = None
count_consecutive_numbers = 1
i = 0
try_again = True
while try_again == True:
	credit_card_number_in_string_type = input('Enter a valid credit card number of ABCD bank:')
# Program accepts a hyphen between 2 digits, but declines multiple hyphens, letters, weird characters between 2 digits
	if re.search('[4-6]\d{3}-\d{4}-\d{4}-\d{4}', credit_card_number_in_string_type) == None and re.search('[4-6]\d{15}', credit_card_number_in_string_type) == None:
		print('Invalid credit card number!')
		continue
	else:
		credit_card_number_in_string_type = re.sub('-', '', credit_card_number_in_string_type)
# Program declines 4 or more similar digits next to each other
		count_consecutive_numbers = 1
		for i in range(1, len(credit_card_number_in_string_type)):
			if credit_card_number_in_string_type[i] == credit_card_number_in_string_type[i-1]:
				count_consecutive_numbers += 1
			else:
				count_consecutive_numbers = 1
		if count_consecutive_numbers >= 4:
			break
		if count_consecutive_numbers >= 4:
			print('Invalid credit card number!')
			continue
		else:
# I update the code so that program declines leading characters (not digits), trailing characters, integers smaller than 4000000000000000, integers larger than 6999999999999999
			try:
				credit_card_number = int(credit_card_number_in_string_type)
			except Exception:
				print('Invalid credit card number!')
				continue
			if credit_card_number < 4000000000000000 or credit_card_number > 6999999999999999:
				print('Invalid credit card number!')
				continue
			else:
				print('Valid credit card number!')
				try_again = False
				exit()