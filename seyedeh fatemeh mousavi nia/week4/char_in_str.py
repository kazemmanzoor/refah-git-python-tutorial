#char in string
def char_str():
    char=input("char:")
    str=input("str:")
    count_char=0
    for i in range(len(str)):
        if(str[i]==char or str[i]==char.upper()):
            count_char=count_char+1
        else:
            continue
    return count_char
    
    
print(char_str())