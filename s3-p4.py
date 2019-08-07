import sys,string,math
n=int(input())
m=2**n
T=[]
for i in range (0,m):
    l=bin(i)[2:]
    j=len(l)
    if j < n:
      l='0' *(n-j)+l
    T.append(l)
for i in range (0,len(T)):
  print(T[i])   
