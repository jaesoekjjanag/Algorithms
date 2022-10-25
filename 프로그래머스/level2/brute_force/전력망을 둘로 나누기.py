from collections import defaultdict

def solution(n, wires):
    answer = n
    tree = defaultdict(list)
    
    def dfs(k, visited):
      visited.append(k)
      
      for t in tree[k]:
        if t in visited: 
          continue
      
        dfs(t, visited)
    
    
    for w in wires:
        v1, v2 = w
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    for k in tree.keys():
      for v in tree[k]:
        visited1 = [k]
        visited2 = [v]
        dfs(v, visited1)
        dfs(k, visited2)
        
        gap = abs((len(visited1) - 1) - (len(visited2)-1))
        answer = min(answer, gap)
              
    return answer
  
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))