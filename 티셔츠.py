people = [2, 3]
tshirts = [1, 2, 3]

def solution(people, tshirts):
  p = t = 0
  count = 0
  
  while(p < len(people) and t < len(tshirts)):
    if people[p] <= tshirts[t]:
      p += 1
      t += 1
      count += 1
    else:
      t += 1 
  
  return count 

print(solution([2,3,4], [1,2,3]))
print(solution([2,3], [1,2,3]))
print(solution([1,2,3], [1,1]))

