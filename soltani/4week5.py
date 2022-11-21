matn = "hello word welcome"
def myfunc(func):
    listeman = {}
    mylist=list(func.upper())
    for item in mylist:
        if ['A','O','E','I','U','Y'].count(item)>0:
            listeman[item]=listeman.get(item , 0)+1
    return listeman
print(myfunc(matn))
