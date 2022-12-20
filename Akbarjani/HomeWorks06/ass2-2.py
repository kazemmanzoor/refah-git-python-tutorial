import requests
data = requests.get('https://one-api.ir/danestani/?token=182191:63a1e19b44e3a2.95228061')
print(data.json()['result']["Content"])
