# 순환인지 파악. dfs를 돌며 선수과목을 하나씩 더해가고, 배우고자 하는 과목이 선수과목 안에 있으면 false를 반환 

# 2 1, 1 0, 0 2
from collections import defaultdict

def solution(n, courses):
  require = []
  for a, b in courses:
    require.append(b)
    if a in require:
      return False
    
  return True

print(solution(2, [[1,0], [0,1]]))
print(solution(2, [[1,0]]))