def func(l):
    ans_list=[]
    for j in l:
        sor = 0
        for i in j:
            sor = sor + i
        ans_list.append(sor)
    return ans_list


data_list = [ int(x) for x in input("Enter your list (multiple value): ").split() ]
output = func(data_list)
print("The output list is:",output)

