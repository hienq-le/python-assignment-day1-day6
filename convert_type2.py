# Find a specific folder, then convert all the json, yaml files inside to csv, all the csv files inside to json
import re, pandas, argparse, os, yaml, subprocess
list_of_json_files = []
list_of_yaml_files = []
list_of_csv_files = []
file_name = None
file_name2 = None
file_name3 = None
temp_obj = None
folder_name_to_find = None
count_converted_files = 0
parser3 = argparse.ArgumentParser(description = 'Find a specific folder, then convert all the json, yaml files inside to csv, all the csv files inside to json')
parser3.add_argument('folder_to_find', type = str, metavar = 'Subdirectory to convert files inside', help = 'Specify the folder name. It will look for files inside to convert')
args6 = parser3.parse_args()
folder_name_to_find = args6.folder_to_find
if folder_name_to_find == None:
    print('Couldn\'t specify a folder name')
    exit()
if os.path.exists('.\\' + folder_name_to_find + '\\') == False:
    os.system('mkdir .\\' + folder_name_to_find)
os.chdir('.\\' + folder_name_to_find)
temp_obj = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
list_of_json_files = re.findall('[^\\\'\"/&?!:*%\x5E\x20\b\t\n]+.json', temp_obj)
second_list_of_json_files = re.findall('\"[^\\\'\"/&?!:*%\x5E\b\t\n]+.json\"', temp_obj)
for ab in second_list_of_json_files:
    list_of_json_files.append(ab)
list_of_yaml_files = re.findall('[^\\\'\"/&?!:*%\x5E\x20\b\t\n]+.yaml', temp_obj)
second_list_of_yaml_files = re.findall('\"[^\\\'\"/&?!:*%\x5E\b\t\n]+.yaml\"', temp_obj)
for cd2 in second_list_of_yaml_files:
    list_of_yaml_files.append(cd2)
list_of_csv_files = re.findall('[^\\\'\"/&?!:*%\x5E\x20\b\t\n]+.csv', temp_obj)
second_list_of_csv_files = re.findall('\"[^\\\'\"/&?!:*%\x5E\b\t\n]+.csv\"', temp_obj)
for ef in second_list_of_csv_files:
    list_of_csv_files.append(ef)
if len(list_of_json_files) == 0 and len(list_of_yaml_files) == 0 and len(list_of_csv_files) == 0:
    print('Couldn\'t convert files!')
else:
    for file_name in list_of_json_files:
        try:
            file2 = pandas.read_json(file_name, orient='records')
        except ValueError:
            continue
        file2.to_csv(file_name.strip('.json') + '.csv', index = None, header = True)
        count_converted_files += 1
    for file_name2 in list_of_yaml_files:
        file4 = open(file_name2, 'r')
        file5 = yaml.safe_load(file4)
        file4.close()
        file5 = pandas.json_normalize(file5)
        try:
            if file5.empty == True:
                raise ValueError
        except ValueError:
            continue
        file5.to_csv(file_name2.strip('.yaml') + '.csv', index = None, header = True)
        count_converted_files += 1
    for file_name3 in list_of_csv_files:
        try:
            file62 = pandas.read_csv(file_name3)
        except ValueError:
            continue
        file62.to_json(file_name3.strip('.csv') + '.json', orient='records')
        count_converted_files += 1
    if count_converted_files > 0:
        print('Files converted!')
    else:
        print('Couldn\'t convert files!')
os.system('popd')