import requests, mapbox, pycurl, certifi,json, urllib.parse, pprint, person, xlrd
from io import BytesIO 

api_key = open("key.txt", "r").read()
# print(api_key)
pp = pprint.PrettyPrinter(indent=4)
def curl_and_ret_resp(url):
	b_obj = BytesIO() 
	crl = pycurl.Curl() 
	# Set URL value
	crl.setopt(crl.URL, url)
	#use mozilla certificate chain
	crl.setopt(pycurl.CAINFO, certifi.where())
	# Write bytes that are utf-8 encoded
	crl.setopt(crl.WRITEDATA, b_obj)

	# Perform a file transfer 
	crl.perform() 

	# End curl session
	crl.close()

	# Get the content stored in the BytesIO object (in byte characters) 
	get_body = b_obj.getvalue()

	resp = get_body.decode('utf8')
	return resp
def coords_from_addr(addr, bias_to_blacksburg=True):

	addr = urllib.parse.quote(addr)

	if bias_to_blacksburg:
		url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + addr + ".json?proximity=-80.4139,37.2296&access_token=" + api_key
	else:
		url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + addr + ".json?access_token=" + api_key
	# response = requests.request("GET", url)

	resp = curl_and_ret_resp(url)
	data = json.loads(resp)
	
	# print(pp.pprint(data))
	return data['features'][0]['geometry']['coordinates']

# source = input()
# dest = input()
def trip_time(loc1, loc2):
	coords1 = coords_from_addr(loc1)
	coords2 = coords_from_addr(loc2)
	print(coords1)
	url = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving/" +\
	 str(coords1[0]) + ',' + str(coords1[1]) + ";" + str(coords2[0]) + ',' + str(coords2[1]) + "?access_token=" + api_key

	return json.loads(curl_and_ret_resp(url))

def get_duration(trip):
	return(trip['trips'][0]['legs'][0]['duration'])

def get_distance(trip):
	trip['trips'][0]['legs'][0]['distance']

def read_excel(fname):
	wb = xlrd.open_workbook(fname)
	sheet = wb.sheet_by_index(0)
	people = []

	for i in range (1, sheet.nrows):
		p = None
		# print(sheet.cell_value(i,0))
		if sheet.cell_value(i,2) == "Yes":
			p = person.Person(\
				sheet.cell_value(i,0),\
				sheet.cell_value(i,1),\
				True,\
				seats=sheet.cell_value(i,3),\
				mpg=sheet.cell_value(i,4))
		else:
			p = person.Person(\
				sheet.cell_value(i,0),\
				sheet.cell_value(i,1))
		people.append(p)
	return people
def find_shortest(people, drivers):
	for d in drivers:
		

p = person.Person("Colin", "")
p2 = person.Person("Greta", "")
# trip = trip_time(p.addr,p2.addr)
# print(pp.pprint(trip))

people = read_excel("Address Sheet_CR.xlsx")
drivers = []
for p in people:
	if p.is_driver:
		drivers.append(p)

