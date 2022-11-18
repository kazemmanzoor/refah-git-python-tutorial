my_dict={
         "zahra":[100,80,78],
         'maryam':[10,80,78],
         'fatemeh':[90,78,81],
         'tahereh':[95,83,79]
      }
count=0
for i in my_dict:
    for j in my_dict[i]:
        if(j>=78):
            count=count+1
    if(count==3):
       print(i)
    count=0
         
           
