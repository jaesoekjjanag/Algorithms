from typing import Counter


tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'D']
n = 2 #n 간격 내에는 동일한 태스크를 실행할 수 없음

# A B C D / A B idle /A idle idle /A

counter = Counter(tasks)
result = 0

while True:
  count = 0
  for task, _ in counter.most_common(n+1):
    count += 1
    counter.subtract(task)
    
    if not counter[task]:
      counter.pop(task)
  
  print(count)  
  if not counter:
    break

