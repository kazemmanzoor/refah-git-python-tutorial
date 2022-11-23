def str_reverser(string):
 new = ''
 splited = string.split(' ')
 for i in splited:
 rvs = list(i+' ')
 rvs.reverse()
 for j in rvs:
 new = new + j
 return new
my_str = input('your string:\t')
print(str_reverser(my_str))
your string: salam man Hadis hastam
 malas nam sidaH matsah
# strr = "salam khoobi chetori"
# str2 = ''
# ls = strr.split(' ')
# a = list(ls[0])
# a.reverse()
# for i in a:
# str2 = str2 + i
# str2

{"type":"string"}
import pandas as pd
import numpy as np

csv_file = pd.read_csv('scipo1939-estimated-population-country-byprovince-1398-fa.csv')
my_df = pd.DataFrame(csv_file)
my_df.rename(columns={'ها‌استان' :'Provinces', 'نفر' :'Population'},
inplace=True)
my_df
 Provinces Population
آذربایجان شرقی 4018000 0
آذربایجان غربی 3398000 1
2 1297000 اردبیل
3 5292000 اصفهان
4 2865000 البرز
5 597000 ایالم
6 1230000 بوشهر
7 13807000 تهران
چهارمحال وبختیاری 979000 8
خراسان جنوبی 809000 9
خراسان رضوی 6768000 10
خراسان شمالی 892000 11
12 4885000 خوزستان
13 1095000 زنجان
14 750000 سمنان
سیستان وبلوچستان 2978000 15
16 5006000 فارس
17 1322000 قزوین
18 1373000 قم
19 1658000 كردستان
20 3299000 كرمان
21 1989000 کرمانشاه
کهگیلویه وبویراحمد 744000 22
23 1951000 گلستان
24 2562000 گیالن
25 1793000 لرستان
26 3365000 مازندران
27 1467000 مرکزی
28 1902000 هرمزگان
29 1771000 همدان
30 1213000 یزد
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

csv_file = pd.read_csv('scipo1939-estimated-population-country-byprovince-1398-fa.csv')
my_df = pd.DataFrame(csv_file)
my_df.rename(columns={'ها‌استان' :'Provinces', 'نفر' :'Population'},
inplace=True)
# x = my_df.columns.to_list()
x = np.array(my_df['Provinces'])
y = np.array(my_df['Population'])
plt.rcParams["figure.figsize"] = (15,15)
plt.barh(x, y, height=0.8)
<BarContainer object of 31 artists>
def palindrome(string):
 return string == string[::-1]
input_ = input('your string:\t')
if palindrome(input_) == True:
 print('Yes')
else:
 print('No')
your string: SALAS
Yes