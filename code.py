Coding:
  
n=int(input())
a=[]
while n>0:
    a.append(n%10)
    n=int(n/10)
print(max(a))
