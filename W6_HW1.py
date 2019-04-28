import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# URL
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_221992.json (Sum ends with 71)

# Void Setup
url = 'http://py4e-data.dr-chuck.net/comments_221992.json'
state = True  # to control the break of void loop
lst_of_counts = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Void Loop
while state:
    print('Retrieving URL: ', url)  
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode() 

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())

    for u in js['comments']:
        lst_of_counts.append(u['count']) # to store the values extracted into the list
    state = False

print('The final total count: ' + str(sum(lst_of_counts)))
        
