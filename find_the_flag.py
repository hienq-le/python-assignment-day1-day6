import re, os
i = 0
f_check = True
file_name = None
string_to_find_flag = None
flag_found = False
while f_check == True:
    file_name = '.\\find_the_flag\\' + str(i) + '.txt'
    f_check = os.path.exists(file_name)
    if f_check == False:
        break
    else:
        current_file = open(file_name, 'r')
        string_to_find_flag = current_file.read()
        if len(re.findall('}', string_to_find_flag)) > 0:
            flag_found = True
            print('Flag found!')
            print('Flag is: ' + string_to_find_flag)
            print('File with flag: ' + file_name)
            current_file.close()
            break
        current_file.close()
        i += 1
        continue
if flag_found == False:
    print('Flag not found!')