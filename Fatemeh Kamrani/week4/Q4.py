def func(str):
    inarr = str.split(" ")
    outarr = []
    for i in range(len(inarr)):
        outarr.append(inarr[i][::-1])
    return " ".join(outarr)
        
str1 = "salam salam salam"
print(func(str1))