import requests
import smtplib

MY_LAT = 54.516247
MY_LNG = -6.058011
ISS_LAT = 0
ISS_LNG = 0
parameter = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}


def makeRequest():
    global ISS_LAT, ISS_LNG
    iss_response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    data = iss_response.json()
    # print(data)
    ISS_LAT = data['latitude']
    ISS_LNG = data['latitude']


def getTime():
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameter, )
    response.raise_for_status()
    data = response.json()
    print(data['results']['sunset'].split('T')[1].split("+")[0])
    print(data['results']['sunrise'].split('T')[1].split("+")[0])


def sendMessage():
    my_email = "venedygait@gmail.com"
    password = 'wafx kraj qzem rhmu'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='venedygait@gmail.com', msg='Look up!!!')


makeRequest()
getTime()
# if MY_LNG == ISS_LNG and MY_LAT == ISS_LNG:
