import requests
from tkinter import *

data = requests.get('https://one-api.ir/hafez/?token=111625:639af4e847e461.34086245')
poem = data.json()['result']['RHYME']
translate = data.json()['result']['MEANING']

root = Tk()

root.title("فال حافظ")
root.geometry("450x650")

label = Label(root, text =poem).pack()

root.mainloop()




