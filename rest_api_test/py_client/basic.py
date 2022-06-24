import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint) #HTTP REQUEST
print(get_response.text) #print raw text response

# HTTP REQUEST WILL GIVE YOU ----> HTML
# REST API REQUEST -----> JSON(XML)



# JAVA SCRIPT OBJECT NOTATION:
#
# "data": "",
# "files": {},
# "form": {},
# "headers": {},
# "JSON": null,
# "method": "GET",
# "origin": "192.63.174.213",
# "url": "https://httpbin.org/anything"
#
#JAVA SCRIPT OBJECT NOTATION: