def unique_selctor(ls_1, ls_2):
 result = []
 ls_3 = [i for i in ls_1 for j in ls_2 if i == j]
 for i in ls_3:
 if i not in result:
 result.append(i)
 return result
ls_1 = list(input('list 1: \n').split('.'))
ls_2 = list(input('list 2: \n').split('.'))
print(unique_selctor(ls_1, ls_2))
list 1:
1.2.3.45.2.2.7
list 2:
3.2.2.2.1
['1', '2', '3']
def odd_selector(ls):
 odds = []
 for i in range(len(ls)):
 if int(ls[i]) % 2 != 0:
 odds.append(int(ls[i])+1)
 if int(ls[i]) % 2 == 0:
 odds.append(int(ls[i]))

 return odds
my_ls = list(input('your list: ').split('.'))
print(odd_selector(my_ls))
your list: 1.4.3.7.8.10.11.9
[2, 4, 4, 8, 8, 10, 12, 10]
def sorted_lists(ls_1, ls_2):
 ls_3 = []

 for i in ls_1:
 if int(i) not in ls_3:
 ls_3.append(int(i))
 for j in ls_2:
 if int(j) not in ls_3:
 ls_3.append(int(j))
 return sorted(ls_3,reverse=True)
ls_1 = list(input('list 1: ').split('.'))
ls_2 = list(input('\nlist 2: ').split('.'))
print(sorted_lists(ls_1, ls_2))
list 1: 1.2.3.7.4.5.6.6
list 2: 6.7.5.8.9.8.10
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def pop_last_first(ls):
 ls.pop(0)
 ls.pop(-1)
 return ls
ls = list(input('your list: ').split('.'))
print(pop_last_first(ls))
your list: 1.2.'three'.4.5.6
['2', "'three'", '4', '5']