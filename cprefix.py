st = int(input())
e=[]
for i in range(0,st):
 inpu=input()
 e.append(inpu)
li=[]
for i in zip(*e):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
