import requests
from tkinter import *

data = requests.get('https://one-api.ir/danestani/?token=111625:639af4e847e461.34086245')
danestani = data.json()['result']['Content']
print(danestani)
root = Tk()

root.title("فال حافظ")
root.geometry("450x450")

label = Label(root, text =danestani).pack()

root.mainloop()




