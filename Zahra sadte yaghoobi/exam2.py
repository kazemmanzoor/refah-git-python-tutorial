j = "my name is zahra sadate yaghoobi"


def n_letter_dictionary(string1):
    list1 = string1.split(" ")
    diction = {}
    for i in list1:
        diction[len(i)] =diction.get(len(i) , " ")+" "+ i
        print(diction)
    return diction

print(n_letter_dictionary(j))
