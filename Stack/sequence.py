top = 0
s1 =[]
s2 =[]

result = []

def sequence(n):
  global top, s1, s2
  try:
    if n > top:
      start = top + 1
      while start <= n:
        s1.append(start)
        start +=1
        result.append('+')
      popped = s1.pop()
      result.append('-')
      s2.append(popped)
      top = popped
    else:
      popped = ''
      while popped != n:
        popped = s1.pop()
        result.append('-')
  except IndexError:
    result.append('NO')

n = int(input())
for _ in range(n):
  sequence(int(input()))

if('NO' in result):
  print('NO')
else:
  for i in result:
    print(i)
