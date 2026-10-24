def f(a):
 x=0
 for i in a:
  x=x+i
 y=x/len(a)
 if y>=90:
  print("A")
 elif y>=75:
  print("B")
 elif y>=60:
  print("C")
 else:
  print("F")
 return y
l=[88,92,79]
m=[55,61,70]
f(l)
f(m)
