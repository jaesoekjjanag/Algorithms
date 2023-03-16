import sys
input = sys.stdin.readline

n = int(input())
consult = [list(map(int, input().split())) for _ in range(n+1)]
dp = [0] * (n+1)

for i in range(len(consult)-2, -1, -1):
  t, p = consult[i]
  if i+t <= n:
    dp[i] = max(p + dp[i+t], dp[i+1])
  else:
    dp[i] = dp[i+1]
    
print(dp[0])