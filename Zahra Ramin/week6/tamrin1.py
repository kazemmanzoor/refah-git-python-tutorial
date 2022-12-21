import requests
import json
def getSunSet(lat , lng):
    reqSentece = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)
    responseApi = requests.get(reqSentece);

    return responseApi.text

print("sunrise: ", ans.get("sunrise") , "\nsunset: ",ans.get("sunset"))
ans =json.loads( getSunSet(36.305729, 59.57837)).get("results")
