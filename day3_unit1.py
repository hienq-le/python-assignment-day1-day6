import re
credit_card_number = 0
credit_card_number_in_string_type = None
count_consecutive_numbers = 1
i = 0
try_again = True
while try_again == True:
    credit_card_number_in_string_type = input('Enter a valid credit card number of ABCD bank:')
    if re.search('[4-6]\d{3}-\d{4}-\d{4}-\d{4}', credit_card_number_in_string_type) == None and re.search('[4-6]\d{15}', credit_card_number_in_string_type) == None:
        print('Invalid credit card number!')
        continue
    else:
        credit_card_number_in_string_type = re.sub('-', '', credit_card_number_in_string_type)
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
        credit_card_number = int(credit_card_number_in_string_type)
        print('Valid credit card number!')
        try_again = False
        exit()