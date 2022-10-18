def multiple(g,h):
    if g%h==0:
        return "<true>"
    elif g == 0:
        return "<False>"
    else:
        return "<False>"
g=int(input(" number 1: "))
h=int(input(" number 2: "))
print("----------------------------------------------------------------")
print("your answer is:", multiple(g,h))
