import re, pandas, argparse, os, yaml, subprocess
list_of_json_files = []
list_of_yaml_files = []
list_of_csv_files = []
file_name = None
file_name2 = None
file_name3 = None
temp_obj = None
folder_name_to_find = None
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
list_of_yaml_files = re.findall('[^\\\'\"/&?!:*%\x5E\x20\b\t\n]+.yaml', temp_obj)
list_of_csv_files = re.findall('[^\\\'\"/&?!:*%\x5E\x20\b\t\n]+.csv', temp_obj)
if len(list_of_json_files) == 0 and len(list_of_yaml_files) == 0 and len(list_of_csv_files) == 0:
    print('Couldn\'t convert files!')
else:
    for file_name in list_of_json_files:
        file2 = pandas.read_json(file_name)
        file2.to_csv(file_name.strip('.json') + '.csv')
    for file_name2 in list_of_yaml_files:
        file4 = open(file_name2, 'r')
        file5 = yaml.safe_load(file4)
        file4.close()
        file5 = pandas.json_normalize(file5)
        file5.to_csv(file_name2.strip('.yaml') + '.csv')
    for file_name3 in list_of_csv_files:
        file62 = pandas.read_csv(file_name3)
        file62.to_json(file_name3.strip('.csv') + '.json')
    print('Files converted!')
os.system('popd')