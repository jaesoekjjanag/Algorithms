grid1 = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]

grid2 = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]

def solution(grid):
  result = 0 
  
  def dfs(x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
      return
    
    if grid[x][y] == 0:
      return
    
    grid[x][y] = 0
    
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        dfs(i, j)
        result += 1
      
  return result

print(solution(grid1))
print(solution(grid2))