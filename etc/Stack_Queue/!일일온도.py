#더 따뜻한 날은 최소 며칠 뒤인가?

T = [73, 74, 75, 71, 69, 72, 76, 73]

def solution(T):
  result = [0]*len(T)
  stack = []
  for i, cur in enumerate(T):
    while stack and cur > T[stack[-1]]:
      last = stack.pop()
      result[last] = i - last
    stack.append(i)
  return 

print(solution(T))