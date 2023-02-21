# n = int(input())

# dp = [0]*10001
# dp[1] = 1
# dp[2] = 3

# for i in range(3, n+1):
#   tmp = 0
#   for j in range(1, i//2+1):
#     if(j//2):
#       tmp += dp[j] * dp[i-j]
      
#     if(not j//2):
#       tmp += 2*(dp[j] * dp[i-j])
  
#   dp[i] = tmp - (i-2)

# print(dp[n])