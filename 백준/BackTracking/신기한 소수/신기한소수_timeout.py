# 에라토스테네스의 체로 풀이하려 했으나 시간 초과

def dfs(dp, n):
  if dp[int(n)] == 1:
    return False
  
  length = len(n)
  if length == 1 and dp[int(n)] == 0:
    return True
  
  return dfs(dp, n[:length-1])

def solution(N):
  max_num = 10**N
  dp = [0] * (max_num + 1)
  dp[0] = 1
  dp[1] = 1
  
  for i in range(2, max_num):
    s = 2
    while True:
      crnt = i*s
      if crnt > max_num:
        break
      dp[crnt] = 1
      s += 1
  
  for i in range(int(max_num/10), max_num):
    if dfs(dp, str(i)):
      print(i)
  
solution(4)