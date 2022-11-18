list1 = "my name is elahe"

def fum (list):
    arey =list.split(" ")
    list2 = []
    for i in range(len(arey)):
        list2.append(arey[i][::-1])
    return " ".join(list2)
        
print(fun(list1))
