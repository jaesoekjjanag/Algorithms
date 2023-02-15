# 첫 줄에 물품의 수 N과 최대로 담을 수 있는 무게 K
# 물건의 무게 W, 가치 V
# 최대로 담을 수 있는 가치 

import sys

# f = open("평범한배낭.txt")

n, k = map(int, input().split())
items = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, k+1):
    not_taking_value = dp[i-1][j]
    
    weight = items[i-1][0]
    value = items[i-1][1]
    
    if j >= weight:
      taking_value = dp[i-1][j-weight] + value
      dp[i][j] = max(not_taking_value, taking_value)
    else: #무게 초과로 집을 수 없는 경우
      dp[i][j] = not_taking_value
    
print(dp[n][k])