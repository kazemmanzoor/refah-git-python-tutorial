import requests
data=requests.get("https://one-api.ir/hafez/?token=450914:63b4486cdf40e9.83317004")
print(data.json()['result']["meaning"])

