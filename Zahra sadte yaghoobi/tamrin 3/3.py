originalList2 = [2, -1, -2, 0, 1]
for i in originalList2[1:]:
    j = originalList2.index(i)
    while j > 0 and originalList2[j-1] < originalList2[j]:
        originalList2[j], originalList2[j-1] = originalList2[j-1], originalList2[j]
        j = j - 1
print(originalList2)
