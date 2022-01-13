# def solution(a, b):
#   if(b == 1):
#     return a
  
#   left = b//2
#   right = b - b//2
  
#   return solution(a, left)%c * solution(a, right)%c

# a, b, c = map(int, input().split())
# print(solution(a%c,b)%c)

def solution(a, b, c):
  if(b == 1):
    return a%c
  
  result = solution(a, b//2, c)
  
  if(b%2 == 0):
    return result * result % c
  else:
    return result * result * a % c
  
a, b, c = map(int, input().split())
print(solution(a,b, c))