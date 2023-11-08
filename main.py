import requests
MY_LAT=54.516247
MY_LON=-6.058011
#
#
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# print(data)

parameter = {
    'lat':MY_LAT,
    'lng':MY_LON,
    'formatted':0
}

response = requests.get('https://api.sunrise-sunset.org/json',params=parameter,)
response.raise_for_status()
data =response.json()
print(data['results']['sunset'].split('T')[1].split("+")[0])
print(data['results']['sunrise'].split('T')[1].split("+")[0])
