maghadir={"fatemeh":[17,10,19],"maryam":[19,20,19],"hanie":[17,19,18]}
def myfunc(func):
    listname=[]
    listkeys=list(func.keys())
    for item in listkeys:
      grades=func.get(item)
      count=0
      for i in grades:
          if i>18:
             count=count+1
      if count==len(grades):
            listname.append(item)
    return listname
print(myfunc(maghadir))
