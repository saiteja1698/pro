p=int(input())
li=list(map(int,input().split()))
q=li[:p//2]
r=li[p//2:]
if(sum(q)//len(q)==sum(r)//len(r)):
	print('yes')
	exit()
print('no')
