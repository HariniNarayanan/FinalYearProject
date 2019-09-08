import urllib.request as ullb
import json

endpoint  = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'AAIzaSyCtdj36-nzvVOxIguEZ7Dsig8dWGIPKE8A'
units = 'units=metric&'
origin = input("ORIGIN: ").replace(" ", "+")
destination = input("DESTINATION: ").replace(" ", "+")
nav_request = 'origins={}&destinations={}&key={}'.format(origin, destination, api_key)
request = endpoint + nav_request
response = ullb.urlopen(request).read()
result = json.loads(response)
print(result)
