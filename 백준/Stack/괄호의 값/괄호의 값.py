# (): 2
# []: 3
# (x): 2*val(x)
# [x]: 3*val(x)
# xy: val(x) + val(y)

# f = open("괄호의 값.txt")
import sys
# braces = f.readline().rstrip()
braces = sys.stdin.readline().rstrip()
op = {'(': 2, '[' : 3, ')': 2, ']': 3}
pair = {')': '(', ']': '['}
o_br = ['(', '[']
c_br = [')', ']']

def solution():
  stack = []
  total = 0
  temp = 1
  last = ''
  
  for i in braces:
    if i in o_br:
      stack.append(i)
      temp *= op[i]
      
    if i in c_br:
      if not stack:
        return 0
      
      top = stack.pop()
      if pair[i] != top:
        return 0

      if pair[i] == last:
        total += temp
      temp //= op[i]
      
    last = i 
    
  
  return total  

print(solution())