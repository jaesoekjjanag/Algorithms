f = open("./듣보잡.txt")
n, m = map(int, f.readline().rstrip().split())

listen = sorted([f.readline().rstrip() for _ in range(n)])
see = sorted([f.readline().rstrip() for _ in range(m)])

lp = 0
sp = 0

listen_see =[] 
while(lp < len(listen) and sp < len(see)):
  if listen[lp] == see[sp]:
    listen_see.append(listen[lp])
    lp += 1
    sp += 1
  elif listen[lp] < see[lp]:
    lp += 1
  elif see[lp] < listen[lp]:
    sp += 1

length = len(listen_see)
print(length)
for i in range(length):
  print(listen_see[i])


  