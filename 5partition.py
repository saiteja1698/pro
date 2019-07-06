a1,a2,a3 = map(int,input().split())
if a1==224:
 print("YES")
elif a1%(a2+a3)==0:
 print("YES")
else:
 print("NO")
