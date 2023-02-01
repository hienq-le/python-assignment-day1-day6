import requests, re, csv, pandas
from parsel import Selector
input_url = 'https://www.cisa.gov/uscert/ncas/alerts'
input_url2 = 'https://www.cisa.gov/uscert/ncas/alerts/2023'
warning_list = []
temp_object = None
temp_object2 = []
temp_object3 = None
header = ['Alert ID', 'Alert Name', 'Release Date', 'Last Revised', 'Tips', 'Alert Link']
iterator_warning = None
file_name1 = 'uscert_warnings_2023.csv'
file_name2 = 'uscert_warnings_2023.xlsx'
file1 = None
file2 = None
csv_writer = None
count = 0
temp_object = requests.get(input_url2)
temp_object2 = temp_object.text.splitlines()[290:500]
temp_object3 = ''.join(temp_object2)
selector = Selector(text=temp_object3)
warning_list = selector.xpath('//li').getall()
count = len(warning_list)
if count == 0:
    print('There are no alerts from US-CERT in 2023!')
else:
    file1 = open(file_name1, 'w', encoding='UTF8', newline='')
    csv_writer = csv.writer(file1)
    csv_writer.writerow(header)
    for iterator_warning in warning_list:
        temp_object11 = re.findall('AA23-\d{3}A', iterator_warning)
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
    print('Successfully wrote alerts from US-CERT in 2023 to '+file_name1+' and '+file_name2)

