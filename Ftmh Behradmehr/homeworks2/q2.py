def gcd(first,second):
      if first > second:
           bmm = second
                 elif second > first:
           bmm = first
                 while bmm > 1:
      if first % bmm == 0 and second % bmm == 0:
               print(f"B.M.M is {bmm}") 
               break
               else:
             bmm -= 1
             if first % bmm == 0 and second % bmm == 0:
                  return print(f"B.M.M is {bmm}")
