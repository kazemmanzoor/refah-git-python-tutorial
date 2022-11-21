def fun(my_string,my_char):
    count=0
    for i in my_string:
        if i==my_char:
            count=count+1

x=input("enter string:")
y=input("enter character:")
ans=fun(x,y)
print(ans)
