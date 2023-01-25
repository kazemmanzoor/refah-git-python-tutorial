import requests
import json

def getSet(lat , lng):
    sentece = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)
    Api = requests.get(reqSentece);
    return Api.text
    

a =json.loads( getSet(36.305729, 59.57837)).get("results")

print("sunrise: ", a.get("sunrise") , "\nsunset: ",a.get("sunset"))
