import sys
input = open('./input.txt').readline
n = int(input())
nums = [int(input()) for _ in range(n)]
max_num = max(nums)

dp = [0]*(max_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for n in range(4, max_num+1):
  dp[n] = sum([dp[n-1], dp[n-2], dp[n-3]])

for n in nums:
  print(dp[n])

