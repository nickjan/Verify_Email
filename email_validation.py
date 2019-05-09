#
import json
import urllib2
email= raw_input('enter email')
url = "http://api.quickemailverification.com/v1/verify?email="+email+"&apikey=your_api_key"
response = urllib2.urlopen(url)
data = response.read()
values = json.loads(data)

# the result is a Python dictionary:
print(values["result"])
#print(values)
