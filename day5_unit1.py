# Export all alerts from US-CERT in the current year to csv, xlsx
import requests, datetime, re, csv, pandas
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
header = ['Alert ID', 'Alert Name', 'Release Date', 'Last Revised', 'Tips', 'Alert Link']
iterator_warning = None
file_name1 = 'uscert_warnings_'+str(current_year)+'.csv'
file_name2 = 'uscert_warnings_'+str(current_year)+'.xlsx'
file1 = None
file2 = None
csv_writer = None
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
# If the number of alerts is 0, print out number of alerts and exit. And if the number of alerts doesn't reach 30, export alerts to csv and xlsx files.
if count == 0:
    print('There are no alerts from US-CERT in ' + str(current_year) + '!')
elif count <= 29:
    file1 = open(file_name1, 'w', encoding='UTF8', newline='')
    csv_writer = csv.writer(file1)
    csv_writer.writerow(header)
    for iterator_warning in warning_list:
        temp_object11 = re.findall('AA\d{2}-[0-9]+[A-Z]', iterator_warning)
        warning_id = temp_object11[0]
        selector2 = Selector(text=iterator_warning)
        warning_name = selector2.xpath('//a[@hreflang="en"]/text()').get()
        alert_link = 'https://www.cisa.gov/uscert/ncas/alerts/'+warning_id
        temp_object12 = requests.get(alert_link)
        temp_object13 = temp_object12.text.splitlines()[250:400]
        temp_object14 = ''.join(temp_object13)
        selector3 = Selector(text=temp_object14)
        temp_object15 = selector3.xpath('//div[@class="submitted meta-text"]').get()
        temp_object16 = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December) [0-9]+, 2023', temp_object15)
        release_date = temp_object16[0].strip('\"')
        last_revised = temp_object16[1].strip('\"')
        tips = 'Not yet'
        line_to_write = [warning_id, warning_name, release_date, last_revised, tips, alert_link]
        csv_writer.writerow(line_to_write)
    file1.close()
    file2 = pandas.read_csv(file_name1)
    file2.to_excel(file_name2, index = None, header = True)
    print('Successfully wrote alerts from US-CERT in '+str(current_year)+' to '+file_name1+' and '+file_name2)
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
# If there is only 1 page, the number of alerts is 30, export alerts to csv and xlsx files
    except Exception:
        file1 = open(file_name1, 'w', encoding='UTF8', newline='')
        csv_writer = csv.writer(file1)
        csv_writer.writerow(header)
        for iterator_warning in warning_list:
            temp_object11 = re.findall('AA\d{2}-[0-9]+[A-Z]', iterator_warning)
            warning_id = temp_object11[0]
            selector2 = Selector(text=iterator_warning)
            warning_name = selector2.xpath('//a[@hreflang="en"]/text()').get()
            alert_link = 'https://www.cisa.gov/uscert/ncas/alerts/'+warning_id
            temp_object12 = requests.get(alert_link)
            temp_object13 = temp_object12.text.splitlines()[250:400]
            temp_object14 = ''.join(temp_object13)
            selector3 = Selector(text=temp_object14)
            temp_object15 = selector3.xpath('//div[@class="submitted meta-text"]').get()
            temp_object16 = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December) [0-9]+, [0-9]+', temp_object15)
            release_date = temp_object16[0].strip('\"')
            try:
                last_revised = temp_object16[1].strip('\"')
            except IndexError:
                last_revised = release_date
            tips = 'Not yet'
            line_to_write = [warning_id, warning_name, release_date, last_revised, tips, alert_link]
            csv_writer.writerow(line_to_write)
        file1.close()
        file2 = pandas.read_csv(file_name1)
        file2.to_excel(file_name2, index = None, header = True)
        print('Successfully wrote alerts from US-CERT in '+str(current_year)+' to '+file_name1+' and '+file_name2)
        exit()
# If there are more than 30 alerts, access next page, look for alerts and repeat until no more alerts and export alerts to csv and xlsx files
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
            file1 = open(file_name1, 'w', encoding='UTF8', newline='')
            csv_writer = csv.writer(file1)
            csv_writer.writerow(header)
            for iterator_warning in warning_list:
                temp_object11 = re.findall('AA\d{2}-[0-9]+[A-Z]', iterator_warning)
                warning_id = temp_object11[0]
                selector2 = Selector(text=iterator_warning)
                warning_name = selector2.xpath('//a[@hreflang="en"]/text()').get()
                alert_link = 'https://www.cisa.gov/uscert/ncas/alerts/'+warning_id
                temp_object12 = requests.get(alert_link)
                temp_object13 = temp_object12.text.splitlines()[250:400]
                temp_object14 = ''.join(temp_object13)
                selector3 = Selector(text=temp_object14)
                temp_object15 = selector3.xpath('//div[@class="submitted meta-text"]').get()
                temp_object16 = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December) [0-9]+, [0-9]+', temp_object15)
                release_date = temp_object16[0].strip('\"')
                try:
                    last_revised = temp_object16[1].strip('\"')
                except IndexError:
                    last_revised = release_date
                tips = 'Not yet'
                line_to_write = [warning_id, warning_name, release_date, last_revised, tips, alert_link]
                csv_writer.writerow(line_to_write)
            file1.close()
            file2 = pandas.read_csv(file_name1)
            file2.to_excel(file_name2, index = None, header = True)
            print('Successfully wrote alerts from US-CERT in '+str(current_year)+' to '+file_name1+' and '+file_name2)
            break
        else:
            continue

