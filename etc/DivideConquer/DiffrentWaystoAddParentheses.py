def solution(expression):
  def compute(left, right, op):
    results = []
    for i in left:
      for j in right:
        results.append(eval(str(i) + op + str(j)))
    return results  
  
  if expression.isdigit():
    return [int(expression)] 
  
  results = []
  
  for i, e in enumerate(expression):
    if e in '+-*':
      left = solution(expression[:i])
      right = solution(expression[i+1:])
    
      results.extend(compute(left, right, e))
  return results