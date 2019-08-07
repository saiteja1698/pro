import sys,string
st = input()
n=len(st)
for j in range (n-2,-1,-1):
  for i in range(0,n-j):
    l, m=i,j+1
    s1=st[l:m + 1]
    if s1>st:
      print(s1)
      sys.exit()
