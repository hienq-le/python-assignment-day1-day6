# Made by Le Quoc Hien with F-Soft account of HienLQ
import requests
from parsel import Selector
input_url = 'https://www.cisa.gov/uscert/ncas/alerts'
input_url2 = 'https://www.cisa.gov/uscert/ncas/alerts/2023'
warning_list = []
temp_object = None
temp_object2 = []
temp_object3 = None
count = 0
temp_object = requests.get(input_url2)
temp_object2 = temp_object.text.splitlines()[290:500]
temp_object3 = ''.join(temp_object2)
selector = Selector(text=temp_object3)
warning_list = selector.xpath('//li').getall()
count = len(warning_list)
if count == 0:
    print('There are no alerts from US-CERT in 2023!')
elif count == 1:
    print('There is 1 alert from US-CERT in 2023.')
else:
    print('There are ' + str(count) + ' or more alerts from US-CERT in 2023.')