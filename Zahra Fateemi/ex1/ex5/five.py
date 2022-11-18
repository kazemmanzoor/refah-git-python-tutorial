def fun(my_dict):
    student=[]
    keys1=list(my_dict.keys())
    for i in keys1:
        count=0
        grade=my_dict.get(i)
        for j in grade:
            if j>=78:
                count=count+1
        if count==len(grade):
            student.append(i)
    return student
dict1={"ahmadi":[65,70,50],"sadeghi":[80,100,89],"fatemi":[95,91,79]}    
print(fun(dict1))
