a=input()
l=[]
for i in a:
  if i not in l:
    l.append(i)
  else:
    break
print(len(l))  
