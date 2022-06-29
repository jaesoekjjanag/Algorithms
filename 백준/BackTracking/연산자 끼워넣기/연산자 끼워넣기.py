# 연산자 순서 + - x /
# 만들 수 있는 최대 값, 최소 값

f = open('연산자 끼워넣기.txt')

n = int(f.readline().rstrip())

A = list(map(int, f.readline().rstrip().split()))
O = list(map(int, f.readline().rstrip().split()))

operators = {
  '+' : O[0],
  '-' : O[1],
  'x' : O[2],
  '/' : O[3],
}


result = []

def dfs(index, sum):
  if(index == n-1):
    result.append(sum)
    return
  
  for o, c in operators.items():
    if c <= 0:
      continue
    
    new_sum = sum
    
    operators[o] -=1
    if o == '+':
      new_sum +=  A[index+1]        
    if o == '-':
      new_sum -=  A[index+1]        
    if o == 'x':
      new_sum *=  A[index+1]        
    if o == '/':
      if ((new_sum < 0 and A[index+1] > 0) or new_sum > 0 and A[index+1] < 0):
        new_sum = (abs(new_sum) // abs(A[index+1])) * -1
      else:
        new_sum = new_sum//A[index+1]        
      
    dfs(index+1, new_sum)
    operators[o] += 1

dfs(0, A[0])

print(max(result))
print(min(result))