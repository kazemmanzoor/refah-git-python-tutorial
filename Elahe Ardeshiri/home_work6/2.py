import requests

password = "670002:639751122ebe54.64905196"
# download video
def downloadVideo(link , token):
    apiSentence = "https://one-api.ir/tiktok/?token={"+token+"}&action=download&link={"+str(link)+"}"
    requests.get(apiSentence)

password = input("enter your password or token: ")
link = input("enter the link of your video: ")
downloadVideo(link , password)


def getNews(rss , token):
    apiSentence = "https://one-api.ir/rss/?token={"+token+"}&action={"+rss+"}"
    requests.get(apiSentence)


password = input("enter your password or token: ")
newsAgencyName = input("enter the name of your news agency:"+
                       +"\n(irinn , tasnim , mehr , irna , mizan or varzesh3... ) ")
ans = getNews(link , password)
print(ans.text())

def getOneRandomJok(token):
    apiSentence = "https://one-api.ir/joke/?token={"+token+"}"
    requests.get(apiSentence)

ans2 = getOneRandomJok(password)
print(ans2.text())
