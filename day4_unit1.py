# Made by Le Quoc Hien with F-Soft account of HienLQ
import urllib.request
import os, re
input_url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
url_to_download_image = None
url_list_from_html = []
des_path = os.environ['USERPROFILE'] + '\\Pictures\\test'
current_image_file_name = None
current_image_file = None
temp_object = None
count = 0
if not os.path.exists(des_path):
    os.makedirs(des_path)
temp_object = urllib.request.urlopen(input_url).read().decode('utf8')
url_list_from_html = re.findall("(//[^\s\"]+)", temp_object)
for i in range(len(url_list_from_html)):
    url_list_from_html[i] = 'https:' + url_list_from_html[i]
url_list_from_html = list(dict.fromkeys(url_list_from_html))
for i in range(len(url_list_from_html)):
    url_to_download_image = url_list_from_html[i]
    if url_to_download_image.endswith('.jpg') or url_to_download_image.endswith('.jpeg') or url_to_download_image.endswith('.png') or url_to_download_image.endswith('.gif') or url_to_download_image.endswith('.webp'):
        tmp_url_to_download_image = url_to_download_image.split('/')
        current_image_file_name = tmp_url_to_download_image[len(tmp_url_to_download_image) - 1]
        try:
            print(urllib.request.urlretrieve(url_to_download_image, des_path + '\\' + current_image_file_name))
        except Exception:
            print('Maximum requests reached! Exit now!')
            if count == 0:
                print('No images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
            elif count == 1:
                print('1 image saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
            else:
                print(str(count) + ' images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
            exit()
        count += 1
    else:
        continue
if count == 0:
    print('No images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
elif count == 1:
    print('1 image saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
else:
    print(str(count) + ' images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')