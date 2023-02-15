#! 시간초과로 실패
# f = open('기타리스트.txt')

# n, s, m = map(int, f.readline().rstrip().split())
# v = list(map(int, f.readline().rstrip().split()))

# fin_volumes = -1

# def dfs(idx, vol):
#   global fin_volumes
  
#   if vol < 0 or vol > m:
#     return
  
#   if idx == n:
#     fin_volumes = max(vol, fin_volumes)
#     return
  
#   diff = v[idx]
  
#   dfs(idx+1, vol+diff)
#   dfs(idx+1, vol-diff)
  
# dfs(0, s)

# print(fin_volumes)

f = open('기타리스트.txt')

n, s, m = map(int, f.readline().rstrip().split())
v = list(map(int, f.readline().rstrip().split()))

dp = [[0]*(m+1) for i in range(n+1)]
dp[0][s] = 1

for i in range(n): 
  for j in range(m+1):
    
    if dp[i][j] == 1:
      diff = v[i] 
      up = j + diff
      down = j - diff
      
      if up <= m:
        dp[i+1][up] = 1
      
      if down >= 0:
        dp[i+1][down] = 1

for i in range(m, -1, -1):
  if dp[n][i] == 1:
    print(i)
    exit(0)
  
print(-1)
