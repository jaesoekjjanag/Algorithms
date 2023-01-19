f = open('./소문난 칠공주.txt')

ip = f.readline

students = [list(ip().rstrip()) for _ in range(5)] 


# 조합으로 Y가 3 이하인, 7개의 점 구하기
# 모든 조합들을 확인.

def T2O(i, j):
  return i*5 + j 
  
def O2T(index):
  return [index//5, index%5]

combinations = []

def getCombinations(index, y, comb):
  [i, j] = O2T(index)
  
  comb.append(index)
  if(students[i][j] == 'Y'):
    y+=1
    
  if(y >= 4):
    return 
  
  if(len(comb) == 7):
    combinations.append(comb[::])
    return 
    
  for i in range(index+1, 25):
    getCombinations(i, y, comb)
    comb.pop()
    

dir = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
def isConnected(c, combination, count):
  answer = 0
  [i, j] = O2T(c)
  combination.remove(c)
  if(count[0] == 7):
    return 1
  
  for [di, dj] in dir:
    [ni, nj] = [i + di, j+dj]
    n = T2O(ni, nj)
    if(0 <= ni <5 and 0 <= nj <5 and n in combination):
      count[0] += 1
      answer += isConnected(n, combination, count)

  return answer      

    

for i in range(19):
  getCombinations(i, 0, [])


answer = 0
for combination in combinations:
  answer += isConnected(combination[0], combination[::], [1])
  
  
print(answer)