m,n=input().split()
o=abs(len(n)-len(m))
for i in range(len(m)):
      if(len(n)==1 and n[i] in m):
          break
      if(m[i]!=n[i]):
        o=o+1
print(o)            
