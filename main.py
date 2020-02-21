import requests, mapbox, pycurl, certifi,json, urllib.parse, pprint
from io import BytesIO 

api_key = open("key.txt", "r").read()
print(api_key)

# source = input()
# dest = input()

b_obj = BytesIO() 
crl = pycurl.Curl() 

addr = input()
addr = urllib.parse.quote(addr)
url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + addr + ".json?proximity=-80.4139,37.2296&access_token=" + api_key
# response = requests.request("GET", url)

# Set URL value
crl.setopt(crl.URL, url)
crl.setopt(pycurl.CAINFO, certifi.where())
# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()


resp = (get_body.decode('utf8'))
data = json.loads(resp)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)