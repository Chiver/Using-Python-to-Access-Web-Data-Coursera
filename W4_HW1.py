from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

num_list = []

for tag in tags:
    num_list.append(int(tag.contents[0]))

print('fucking sum = ' + str(sum(num_list)))

'''
#find the numbers using regular expression
num_list = []


for i in tags:
    num_list.append(int(re.findall('>(0-9)*<', i.contents[0])))

print(sum(num_list))


'''




    








