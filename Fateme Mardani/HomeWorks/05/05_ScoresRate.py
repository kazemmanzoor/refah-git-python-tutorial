def func(dict1):
    person = []
    Keys1 = list(dict1.keys())
    for j in Keys1:
        total = 0
        score = dict1.get(j)
        for i in score:
            if i >= 78:
                total = total + 1
        if total == len(score):
            person.append(j)
    return person


n = 3
input_data = dict(input("Enter key and value: ").split() for _ in range(n))

print("output dict:",func(input_data))
