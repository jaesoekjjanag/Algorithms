n = int(input())
a = list(map(int, input().split()))
a.sort()
x = int(input())

lp = 0
rp = len(a)-1

result = 0

while lp < rp:
  s = a[lp] + a[rp]
  if s == x:
    result += 1
    lp += 1
    rp -= 1
  
  if s < x:
    lp += 1
    
  if s > x:
    rp -= 1
    
print(result)
      