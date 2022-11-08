def func(mystr):
    a= mystr.split(" ")
    b= []
    for i in range(len(a)):
        b.append(a[i][::-1])
    return " ".join(b)

input_string =input("input string:")        
ans=func(input_string)
print("output string: ",ans)
