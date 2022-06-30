# 테케 실패

f = open('스도쿠.txt')
grid = [list(map(int, f.readline().rstrip().split())) for _ in range(9)]

def check_row(r, c, num):
  for i in range(9):
    if num == grid[r][i]:
      return False
  return True

def check_col(r, c, num):
  for i in range(9):
    if num == grid[i][c]:
      return False
  return True

def check_3x3(r, c, num):
  corner_r = r//3*3
  corner_c = c//3*3
  
  for i in range(3):
    for j in range(3):
      if num == grid[corner_r+i][corner_c+j]:
        return False
  return True

def next_location():
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return [i, j]
  # 더이상 채울 공간이 없음 -> 완료
  return [9, 9]

def dfs(r, c, num):
  
  # 종료 조건. 유효하지 않은 숫자 검증
  if not check_row(r, c, num):
    return False
  if not check_col(r, c, num):
    return False
  if not check_3x3(r, c, num):
    return False
  
  grid[r][c] = num
  next_r, next_c = next_location()
  
  if next_r == 9 and next_c == 9:
    for i in grid:
      for j in i:
        print(j, end=' ')
      print()
    exit(0)
  
  # recursion call 조건
  for i in range(1, 10):
    if dfs(next_r, next_c, i):
      return True
    
  grid[r][c] = 0
  return False

start_x, start_y = next_location()
for i in range(9):
  dfs(start_x, start_y, i)

