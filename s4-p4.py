a,b=map(int,input().split())
li=[]
c=0
for i in range(a):
   li.append(input())
for i in range(a):
  for j in range(b-1):
    if li[i][j]=="R" and li[i][j+1]=="R":
      c=c+5
    elif li[i][j]=="G" and li[i][j+1]=="G":
      c=c+3
print(c)        

