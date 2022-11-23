def n_letter_dictionary(str1):
    Mylist=str1.split()
    print(Mylist)
    answer={}
    for item in Mylist:
        val1=answer.get(len(item),[])
        if item in val1:
            continue
        else :
            val2=answer.get(len(item),[] )
            val2.append(item)
            answer[len(item)]=val2
            print(n_letter_dictionary(val1))
    return answer


val="the way you see people is the way you treat them and the way you treat them is what they become"
n_letter_dictionary(val)
