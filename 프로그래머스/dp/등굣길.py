def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i, j in puddles:
        dp[j][i] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            crnt = dp[i][j]
            if crnt != -1:
                if i+1 <= n and dp[i+1][j] != -1:
                    dp[i+1][j] += crnt
                if j+1 <= m and dp[i][j+1] != -1:
                    dp[i][j+1] += crnt
                    
    return dp[n][m] % 1000000007