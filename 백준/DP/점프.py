f = open('점프.txt')

n = int(f.readline().rstrip())
grid = [list(map(int, f.readline().rstrip().split())) for i in range(n)]

dp = [[0]*n for i in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    jump = grid[i][j]
    
    if (jump == 0):
      break
    
    if(dp[i][j] == 0):
      continue
    
    if(i+jump < n):
      dp[i+jump][j] += dp[i][j]
    
    if(j+jump < n):
      dp[i][j+jump] += dp[i][j]
      
print(dp[n-1][n-1])
