def pattern_sum(k,m):
    strnum = k
    count =int(k)
    
    for i in range(m - 1):
        k = k + strnum
        count = count + int(k)
    return(count)


num = input("enter number:")
Rnum = int(input("enter repetition number:"))


print(pattern_sum(num,Rnum))
