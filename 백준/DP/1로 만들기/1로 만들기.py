from collections import deque 

ip = int(input())

dp = [-1]*1000001

dp[ip] = 0

Q = deque([ip])

while(Q):
  crnt = Q.popleft()
  crnt_count = dp[crnt]
  if(crnt == 1):
    print(crnt_count)
    break
  
  if(crnt % 3 == 0):
    nxt = crnt//3
    if(dp[nxt] == -1):
      dp[nxt] = crnt_count + 1
      Q.append(nxt)
    
  if(crnt % 2 == 0):
    nxt = crnt//2
    if(dp[nxt] == -1):
      dp[nxt] = crnt_count + 1
      Q.append(nxt)
  
  nxt = crnt-1
  if(dp[nxt] == -1):
    dp[nxt] = crnt_count + 1
    Q.append(nxt)
  
  
    