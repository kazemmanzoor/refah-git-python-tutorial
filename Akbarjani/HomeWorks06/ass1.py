import requests
import datetime



data=requests.get('https://api.sunrise-sunset.org/json?lat=36.2972&lng=59.6067')
print(data.json()['results']['sunrise'])
print(data.json()['results']['sunset'])