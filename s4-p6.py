import sys,string
a=int(input())
T=[int(x) for x in input().split()]
a=len(T)
count=0
for i in range(0, a-2):
  for j in range(i+1, a-1):
    for k in range(j+1, a):
      if T[i]> T[j] > T[k]:
          count+= 1
print(count)        
