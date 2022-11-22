def func (list):
    arr = list.split(" ")
    newarr = []
    for i in range(len(arr)):
        newarr.append(arr[i][::-1])
    return " ".join( newarr)
