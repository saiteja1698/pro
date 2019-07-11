li = list(input())
lar = 0
for i in range(len(li)):
    t = li[i:len(li)]
    st = list(reversed(t))
    if t == st:
        if lar < len(st):
            lar  = len(st)
for i in range(len(li)):
    t = li[:len(li)-i]
    st = list(reversed(t))
    if t == st:
        if lar < len(st):
            lar = len(st)
print(len(li)-lar)
