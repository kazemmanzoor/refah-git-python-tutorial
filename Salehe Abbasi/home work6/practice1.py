import requests

def getSunSet(lat , lng):
    reqSentece = "https://api.sunrise-sunset.org/json?lat="+str(lat)+"&lng="+str(lng)
    responseApi = requests.get(reqSentece);

    arr1 = responseApi.text.split('"')
    indexSun = arr1.index("sunrise")
    indexTolo = arr1.index("sunset")
    print(arr1 , "   ", indexSun , "   ",indexTolo)

#------------------------------------------------------

getSunSet(36.305729, 59.57837)
