from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

# testing url: http://py4e-data.dr-chuck.net/comments_42.xml
# homework url: http://py4e-data.dr-chuck.net/comments_221991.xml

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Global Variables (Void Setup)
final_outcome = []
url = input('Enter your URL:  ')
xml_input = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml_input)  # the fromstring method returns a tree that contains all nodes
lst_1 = tree.findall('comments/comment')  # the findall returns a list of subtrees

#Void Loop
for item in lst_1:
    final_outcome.append(int(item.find('count').text))

print(sum(final_outcome)) #print('Count: ', item.find('count').text)

    

