def func(my_string,my_char):
    count = 0
    for i in my_string:
        if i == my_char:
            count = count+1
        
a = input("string: ")
b = input("character: ")
ans=func(a,b)
print("answer:",ans)


