dict1=input('insert name?:')
dict2=input('insert score of name?:')
dict3=input('insert score of name?:')
dict4=input('insert score of name?:')
dict5=input('insert name?:')
dict6=input('insert score of name?:')
dict7=input('insert score of name?:')
dict8=input('insert score of name?:')
dict9=input('insert name?:')
dict10=input('insert score of name?:')
dict11=input('insert score of name?:')
dict12=input('insert score of name?:')
my_dict={'dict1':['dict2','dict3','dict4'],
        'dict5': ['dict6','dict7','dict8'],
        'dict9': ['dict10','dict11','dict12']
        }
for value in my_dict.values():
        if  value in dict1:
            value>=78
            print(my_dict[dict1])
            
        
        if  value in dict5:
            value>=78
            print(my_dict[dict5])
         
        
        if  value in dict9:
            value>=78
            print(my_dict[dict9])
else:
    print('is not found')
    
#def top():

    #return my_dict
