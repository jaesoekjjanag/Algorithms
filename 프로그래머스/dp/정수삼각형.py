# i, j => (i+1, j), (i+1, j+1)
def solution(triangle):
    height = len(triangle)
    dp = [[0]*height for _ in range(height)]
    dp[0][0] = triangle[0][0]
    
    for i in range(height):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:  
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]    
                
    return max(dp[height-1])