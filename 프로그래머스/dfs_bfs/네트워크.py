def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    
    def dfs(i):
      visited[i] = 1

      for c in range(n):
        if i != c and computers[i][c] == 1 and visited[c] == 0:
          dfs(c)          
          
    for i in range(n):
      if visited[i] == 0:
        dfs(i)
        answer += 1
        
    return answer
  
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))