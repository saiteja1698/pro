a=int(input())
l=list(map(int,input().split()))
n=[]
s=1
for i in l:
  if i not in n:
    n.append(i)

for i in range(len(n)-1):
         if n[i]<n[i+1]:
           s+=1
print(s)    
