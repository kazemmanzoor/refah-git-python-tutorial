question 2:
a=input("FATEMEH")
baseda=a.count("a")+a.count("o")+a.count("e")+a.count("i")+a.count("u")
print(baseda)

/////

question 3:
def tekrar(a):
    tekrar=a.count(b)
    return tekrar
a=input("word")
b=input("letter")
print(tekrar(a))

/////

question 1:
def isPalindrome (word):
    if word == word[::-1]
       print("true")
    else:
       print("false")
    return word
word= input("insert word")
print(isPalindrome(word))

/////
question 5:
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.plot([
        "Ardabil","Tehran","Qazvin","Kermanshah","Qom","Yazd"],
         [1297000, 13807000,1322000,1989000,1373000,1213000])

plt.title("Population of cities",fontsize=20)
plt.xlabel("Cities")
plt.ylabel("Population")
plt.show()
