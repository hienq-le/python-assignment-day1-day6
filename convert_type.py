import re, pandas, argparse, os, yaml
file_name = None
file_name2 = None
parser3 = argparse.ArgumentParser(description = 'Convert json, yaml formats to csv, xlsx formats')
parser3.add_argument('--input', '-i', type = str, metavar = 'Input file name', required = True, help = 'Specify the input file name. Must be one of json, yaml, csv, xlsx formats')
parser3.add_argument('--output', '-o', type = str, metavar = 'Output file name', required = True, help = 'Specify the output file name. Must be one of json, yaml, csv, xlsx formats. Can\'t be the same format of input file.')
args3 = parser3.parse_args()
file_name = args3.input
file_name2 = args3.output
if file_name == None or file_name2 == None:
    print('Error: couldn\'t specify the input and output file name!')
    exit()    
elif os.path.exists(file_name) == False:
    print('Error: input file '+file_name+' is NOT found!')
    exit()
elif file_name == file_name2:
    print('Error: input and output file names are the same!')
    exit()
elif len(re.findall('.json', file_name + ', ' + file_name2)) == 2 or len(re.findall('.yaml', file_name + ', ' + file_name2)) == 2 or len(re.findall('.csv', file_name + ', ' + file_name2)) == 2 or len(re.findall('.xlsx', file_name + ', ' + file_name2)) == 2:
    print('Error: input and output files have same format!')
    exit()
elif (len(re.findall('.json', file_name)) == 1 and len(re.findall('.yaml', file_name2)) == 1) or (len(re.findall('.yaml', file_name)) == 1 and len(re.findall('.json', file_name2)) == 1):
    print('Error: couldn\'t convert!')
    exit()
elif len(re.findall('.json', file_name)) == 1 and len(re.findall('.csv', file_name2)) == 1:
    file2 = pandas.read_json(file_name)
    file2.to_csv(file_name2)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.json', file_name)) == 1 and len(re.findall('.xlsx', file_name2)) == 1:
    file3 = pandas.read_json(file_name)
    file3.to_excel(file_name2, index = None, header = True)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.yaml', file_name)) == 1 and len(re.findall('.csv', file_name2)) == 1:
    file4 = open(file_name, 'r')
    file5 = yaml.safe_load(file4)
    file4.close()
    file5 = pandas.json_normalize(file5)
    file5.to_csv(file_name2)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.yaml', file_name)) == 1 and len(re.findall('.xlsx', file_name2)) == 1:
    file44 = open(file_name, 'r')
    file55 = yaml.safe_load(file44)
    file44.close()
    file55 = pandas.json_normalize(file55)
    file55.to_excel(file_name2, index = None, header = True)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.csv', file_name)) == 1 and len(re.findall('.json', file_name2)) == 1:
    file6 = pandas.read_csv(file_name)
    file6.to_json(file_name2)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.xlsx', file_name)) == 1 and len(re.findall('.json', file_name2)) == 1:
    file7 = pandas.read_excel(file_name, index = None, header = True)
    file7.to_json(file_name2)
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('.csv', file_name)) == 1 and len(re.findall('.yaml', file_name2)) == 1:
    file8 = pandas.read_csv(file_name).to_dict()
    file9 = open(file_name2, 'w')
    file9.write(file8)
    file9.close()
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
elif len(re.findall('xlsx', file_name)) == 1 and len(re.findall('.yaml', file_name2)) == 1:
    file18 = pandas.read_excel(file_name).to_dict()
    file19 = open(file_name2, 'w')
    file19.write(file18)
    file19.close()
    print('Converted ' + file_name + ' to ' + file_name2 +'!')
else:
    print('Error: couldn\'t convert!')
    exit()