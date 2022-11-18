def func(a):
    b = list(a)
    for i in range(len(b)):
        if (b[i]%2) != 0:
            b[i]=b[i]+1
        else:
            continue
    return b

input_list=[int(x) for x in input("Enter input List:").split()]

ans=func(input_list)
print("output list:",ans)
