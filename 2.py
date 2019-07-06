from itertools import combinations
n ,x = input().split()
x = int(x)
num = []
c = combinations(n,len(n)-x)
for i in c:
    num.append("".join(i))
print(min(num))

