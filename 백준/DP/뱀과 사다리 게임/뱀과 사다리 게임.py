from collections import deque

f = open('./input.txt')
ip = f.readline

n, m = map(int, ip().split())
ladders = {}
dp = [float('inf')] * 101
dp[1] = 0

for _ in range(n):
  k, v = map(int, ip().split())
  ladders[k] = v

for _ in range(m):
  k, v = map(int, ip().split())
  ladders[k] = v

Q = deque([1])
while(Q):
  cur = Q.popleft()
  if(cur in ladders):
    nxt = ladders[cur]
    if(dp[cur] < dp[nxt]):
      dp[nxt] = dp[cur]
      Q.append(nxt)
  
  for i in range(1, 7):
    nxt = cur + i
    if(nxt <= 100 and cur not in ladders and dp[cur] + 1 < dp[nxt]): #! 사다리 또는 뱀인 경우 다음 위치로 곧장 이동해야하므로 주사위를 굴릴 수 없음!!
      dp[nxt] = dp[cur] + 1
      Q.append(nxt)
    
print(dp[100])