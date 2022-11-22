list1=[123,456]
list2=[789,123]
for i in range(len(list1)):
    if(list2.count(list1[i]))>0:
        continue
    else:
        list2.append(list1[i])

print(list2)
