import sys, string, math
n=int(input())
T=[int(x) for x in input().split()]
T.sort()
count=0
for i in range(0,n):
  if T[i]-sum(T[:i]) >= 0:
    count +=1
print(count) 
