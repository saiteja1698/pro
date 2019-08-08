a,b = map(int,input().split())
l = list(map(int,input().split()))
c= 0
for i in l:
    if(i+b <=5):
        c+=1
d=c//3
print(d)
