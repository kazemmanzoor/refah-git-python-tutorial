def func(txt):
    count=0
    for i in txt:
        if i in "aAiIoOuUeE":
            count=count+1
    return count

text=str(input("please enter="))
print(func(text))
