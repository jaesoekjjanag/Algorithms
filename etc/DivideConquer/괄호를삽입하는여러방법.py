s = input()
operators = '+-*/'

def divide(s):
  if len(s) == 1:
    return [s]
  
  results = []
  for i in range(len(s)):
    if s[i] in operators:
      left = divide(s[:i])
      right = divide(s[i+1:])
      
      for l in left:
        for r in right:
          results.append(str(eval(l+s[i]+r)))
  
  return results
      
print(list(map(int, divide(s))))
