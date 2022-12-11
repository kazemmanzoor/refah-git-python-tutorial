import requests

def getSunSet(lat , lng):
    reqSentece = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)
    responseApi = requests.get(reqSentece);

    return responseApi.text.split('"')
    

#------------------------------------------------------

info = getSunSet(36.305729, 59.57837)

indexSun = info.index("sunrise")
indexTolo = info.index("sunset")
print("sunrise: ", info[indexSun+2] , "\nsunset: ",info[indexTolo+2])
