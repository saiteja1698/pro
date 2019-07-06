s,t=input().split()
o=int(s)
i=int(t)
count=0
l=list(map(int,input().split()))
for a in range(o):
    for b in range(a+1,o):
        ss=0
        ss=l[a]+l[b]
        if(ss==i):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
