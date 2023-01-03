import  requests
data= requests.get("https://one-api.ir/weather/?token=450914:63b4486cdf40e9.83317004 &action=current&city={تهران}")
print(data.json()['result'])
