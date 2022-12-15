import requests
from tkinter import *

data = requests.get('https://one-api.ir/sokhan/?token=111625:639af4e847e461.34086245&action=random')
text = data.json()['result']['text']

root = Tk()
root.title("سخن بزرگان")
root.geometry("850x150")
label = Label(root, text =text).pack()
root.mainloop()
