intervals = [[1,3], [2,6], [8,10], [15,10]]

def solution(intervals):
  result = []
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  
  for i in sorted_intervals:
    if result and i[0] <= result[-1][1]:
        result[-1][1] = max(i[1], result[-1][1])
    else:
      result.append(i)
      
  return result
    
print(solution(intervals))