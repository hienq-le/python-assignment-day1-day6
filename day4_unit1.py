# How a Python program downloads all images from a Wikipedia page
import urllib.request, urllib.error
import os, re
input_url = 'https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales'
url_to_download_image = None
hidden_image_list_from_html = []
url_list_from_html = []
des_path = os.environ['USERPROFILE'] + '\\Pictures\\test'
current_image_file_name = None
current_image_file = None
temp_object = None
count = 0
count2 = 0
if not os.path.exists(des_path):
	os.makedirs(des_path)
temp_object = urllib.request.urlopen(input_url).read().decode('utf8')
# Find all images but not in url format from the page, then download them
hidden_image_list_from_html = re.findall("(/[^\s\t\n\'\"\x20:]+)", temp_object)
i = 0
for i in range(len(hidden_image_list_from_html)):
	url_to_download_image = hidden_image_list_from_html[i]
	if url_to_download_image.endswith('.jpg') or url_to_download_image.endswith('.jpeg') or url_to_download_image.endswith('.png') or url_to_download_image.endswith('.gif') or url_to_download_image.endswith('.webp') or url_to_download_image.endswith('.svg'):
		tmp_url_to_download_image = url_to_download_image.split('/')
		current_image_file_name = tmp_url_to_download_image[len(tmp_url_to_download_image) - 1]
		try:
			print(urllib.request.urlretrieve('https://en.wikipedia.org'+url_to_download_image, des_path + '\\' + current_image_file_name))
		except urllib.error.URLError:
			print('Error downloading '+current_image_file_name+'!')
			continue
		except urllib.error.ContentTooShortError:
			print('Error downloading '+current_image_file_name+'!')
			continue
		count2 += 1
		try:
			if hidden_image_list_from_html[i-1].endswith('.jpg') or hidden_image_list_from_html[i-1].endswith('.jpeg') or hidden_image_list_from_html[i-1].endswith('.png') or hidden_image_list_from_html[i-1].endswith('.gif') or hidden_image_list_from_html[i-1].endswith('.webp') or hidden_image_list_from_html[i-1].endswith('.svg'):
				tmp_url_to_download_image2 = hidden_image_list_from_html[i-1].split('/')
				if current_image_file_name == tmp_url_to_download_image2[len(tmp_url_to_download_image2) - 1]:
					count2 -= 1
					continue
		except IndexError:
			print('No images having same name found')
count += count2
# Find all images in url format from the page, then download them
url_list_from_html = re.findall("(//[^\s\t\n\'\"\x20:]+)", temp_object)
for i in range(len(url_list_from_html)):
	url_list_from_html[i] = 'https:' + url_list_from_html[i]
url_list_from_html = list(dict.fromkeys(url_list_from_html))
i = 0
for i in range(len(url_list_from_html)):
	url_to_download_image = url_list_from_html[i]
	if url_to_download_image.endswith('.jpg') or url_to_download_image.endswith('.jpeg') or url_to_download_image.endswith('.png') or url_to_download_image.endswith('.gif') or url_to_download_image.endswith('.webp') or url_to_download_image.endswith('.svg'):
		tmp_url_to_download_image = url_to_download_image.split('/')
		current_image_file_name = tmp_url_to_download_image[len(tmp_url_to_download_image) - 1]
		try:
			print(urllib.request.urlretrieve(url_to_download_image, des_path + '\\' + current_image_file_name))
		except urllib.error.URLError:
			print('Error downloading '+current_image_file_name+'!')
			continue
		except urllib.error.ContentTooShortError:
			print('Error downloading '+current_image_file_name+'!')
			continue
		count += 1
		try:
			if url_list_from_html[i-1].endswith('.jpg') or url_list_from_html[i-1].endswith('.jpeg') or url_list_from_html[i-1].endswith('.png') or url_list_from_html[i-1].endswith('.gif') or url_list_from_html[i-1].endswith('.webp') or url_list_from_html[i-1].endswith('.svg'):
				tmp_url_to_download_image2 = url_list_from_html[i-1].split('/')
				if current_image_file_name == tmp_url_to_download_image2[len(tmp_url_to_download_image2) - 1]:
					count -= 1
					continue
		except IndexError:
			print('No images having same name found')
if count == 0:
	print('No images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
elif count == 1:
	print('1 image saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')
else:
	print(str(count) + ' images saved from \"https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales\"!')