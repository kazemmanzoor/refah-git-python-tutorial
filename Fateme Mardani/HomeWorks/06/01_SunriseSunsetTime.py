# Mashhad Sunrise & Sunset Time
import datetime
import requests
import json

def fanc(lat , lng):
    req = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)
    resApi = req.get(req);

    return resApi.text
  
  
output = json.loads( fanc(36.305729, 59.57837)).get("results")
print("Sunrise: ", ans.get("sunrise") , "\nSunset: ",output.get("sunset"))
