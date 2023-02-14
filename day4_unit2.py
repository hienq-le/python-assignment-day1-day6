# Count all alerts from US-CERT in the current year
import requests, datetime, re
from parsel import Selector
current_date = str(datetime.date.today())
current_date2 = current_date.split('-')
current_year = int(current_date2[0])
input_url = 'https://www.cisa.gov/uscert/ncas/alerts'
input_url2 = 'https://www.cisa.gov/uscert/ncas/alerts/' + str(current_year)
warning_list = []
warning_list2 = []
temp_object = None
temp_object2 = []
temp_object3 = None
temp_object4 = []
temp_object5 = None
temp_object6 = []
temp_object7 = []
temp_object8 = []
temp_object12 = None
temp_object14 = []
temp_object15 = None
temp_object16 = []
max_number_of_pages = 1
count = 0
count2 = 0
i = 1
temp_object = requests.get(input_url2)
temp_object2 = temp_object.text.splitlines()[290:380]
temp_object3 = ''.join(temp_object2)
selector = Selector(text=temp_object3)
temp_object4 = selector.xpath('//li').getall()
for abxy in temp_object4:
    if len(re.findall('AA\d{2}-[0-9]+[A-Z]', abxy)) > 0:
        warning_list.append(abxy)
count = len(warning_list)
# If the number of alerts doesn't reach 30, print out number of alerts and exit
if count == 0:
    print('There are no alerts from US-CERT in ' + str(current_year) + '!')
elif count == 1:
    print('There is 1 alert from US-CERT in ' + str(current_year) + '.')
elif count <= 29:
    print('There are ' + str(count) + ' alerts from US-CERT in ' + str(current_year) + '.')
# If the number of alerts reaches 30, check if there are at least 2 pages
else:
    count += count2
    temp_object6 = temp_object.text.splitlines()[370:500]
    temp_object7 = selector.xpath('//a').getall()
    for abcxyz in temp_object7:
        if len(re.findall('page=[0-9]+', abcxyz)) > 0:
            for abcxyz2 in re.findall('page=[0-9]+', abcxyz):
                temp_object8.append(abcxyz2)
    try:
        max_number_of_pages = int(re.findall('[0-9]+', temp_object8[len(temp_object8) - 1])[0]) + 1
# If there is only 1 page, the number of alerts is 30, print out the number of alerts
    except Exception:
        print('There are ' + str(count) + ' alerts from US-CERT in ' + str(current_year) + '.')
        exit()
# If there are more than 30 alerts, access next page
    
    for i in range(1, max_number_of_pages):
        warning_list2 = []
        count2 = 0
        temp_object12 = requests.get(input_url2 + '?page=' + str(i))
        temp_object14 = temp_object12.text.splitlines()[290:380]
        temp_object15 = ''.join(temp_object14)
        selector2 = Selector(text=temp_object15)
        temp_object16 = selector2.xpath('//li').getall()
        for abxy2 in temp_object16:
            if len(re.findall('AA\d{2}-[0-9]+[A-Z]', abxy2)) > 0:
                warning_list.append(abxy2)
                warning_list2.append(abxy2)
        count2 = len(warning_list2)
        if count2 <= 29:
            count += count2
            print('There are ' + str(count) + ' alerts from US-CERT in ' + str(current_year) + '.')
            break
        else:
            continue
