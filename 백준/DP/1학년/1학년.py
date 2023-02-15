f = open('1학년.txt')

n = int(f.readline().rstrip())
nums = list(map(int, f.readline().rstrip().split()))

dp = [[0 for _ in range(21)] for _ in range(n)]   

target = nums[n-1]
dp[0][nums[0]] = 1

for i in range(1, n-1):
  for j in range(21):
    crnt = dp[i-1][j]
  
    if not crnt:
        continue
    
    val = nums[i]
    
    left = j - val
    right = j + val
    
    if left >= 0:
      dp[i][left] += crnt
      
    if right <= 20 :
      dp[i][right] += crnt
      
print(dp[n-2][target])