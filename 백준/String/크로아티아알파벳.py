def solution(s):
  alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
  flags = ['=', '-', 'j']
  
  count = 0
  
  for i in range(len(s)):
    if s[i] in flags and i<=len(s)-1:
      if i >= 2 and s[i-2 : i+1] == 'dz=':
        count -= 2
      elif i >= 1 and s[i-1 : i+1] in alphabets:
        count -= 1
        
    count += 1
    
  return count

s = input()
print(solution(s))
      
  