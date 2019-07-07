s,t = map(int, input().split())
l = list(map(int, input().split()))
for i in range(t):
  x, y = map(int, input().split())
  print(min(l[x-1:y]))
