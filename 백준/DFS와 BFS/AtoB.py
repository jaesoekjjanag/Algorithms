# A를 B로 만드는데 필요한 최소 연산의 수

a, b = map(int, input().split())

min_time = -1

def dfs(f, t, o):
  global min_time
  if f == t:
    if min_time == -1:
      min_time = o
      return
    
    min_time = min(min_time, o)
    return
  
  if f > t:
    return
  
  a = f*2
  b = int(str(f) + '1')
  
  dfs(a, t, o+1)
  dfs(b, t, o+1)
  
dfs(a, b, 1)
print(min_time)