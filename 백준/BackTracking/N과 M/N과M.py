n, m = map(int, input().split())

nums = list(map(str, range(1, n+1)))

p = set([])

def recursion(str):
  if len(str) == m:
    print(' '.join(list(str)))
    
  for i in nums:
    if i in str:
      continue
    
    recursion(str+i)
    
recursion('')