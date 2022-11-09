def solution(k, dungeons):
    answer = 0
    
    def explore(index, visited, left):
      nonlocal answer
      req, use = dungeons[index]
    
      if left < req:
        answer = max(answer, len(visited))
        return False
    
      visited.append(index)
      left -= use
    
      if len(visited) == len(dungeons):
        answer = len(dungeons)
        return
    
      for i in range(len(dungeons)):
        if i in visited:
          continue
        
        b = len(visited)
        explore(i, visited, left)
        a = len(visited)
        
        if a != b:
          visited.pop()
    
    for i in range(len(dungeons)):
      explore(i, [], k)
      
    return answer
  
# print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(40, [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))