def pattern_sum(val):
    count = val[1]
    sum = 0
    list1 = []
    for item in range(1,count+1):
        mynum =  str(val[0])*item
        sum = sum + int(mynum)
        
        
    return sum


#----------------------------------
myval = [4,5]
print(pattern_sum(myval))
