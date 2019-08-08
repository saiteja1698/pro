import sys,string
def cfreq(a):
    dic={}
    for c in a:
      dic[c]=dic.get(c,0)+1
    return dic

a=input()
n=len(a) 
dic=cfreq(a)  
L=list(dic.keys())

for j in range(n-1,-1,-1):
    for c in L:
       b=0
       for i in range(0,n-j):
           l,r=i,j+1
           a1=a[l:r + 1]
           if c in a1:
              b += 1
       if b==n-j:
          c2=c
          b2=b
          len=j+1
print(len)       
