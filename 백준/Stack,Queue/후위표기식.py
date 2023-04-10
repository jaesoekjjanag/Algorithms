input = open('./후위표기식.txt').readline

infix = input()
operator = {
  '(': 0, 
  '+': 1,
  '-': 1,
  '*': 2,
  '/': 2,
  ')': 3,
}

def itop(infix):
  postfix = []
  stack = []

  for o in infix:
    if(o not in operator):
      postfix.append(o)
      
    elif(o == '('):
      stack.append(o)
      
    elif(o == ')'):
      while(stack[-1] != '('):
        postfix.append(stack.pop())
      stack.pop()
        
    else:
      while(stack and operator[o] <= operator[stack[-1]]): #우선순위가 낮으면 앞선 것들 pop해서 처리
          postfix.append(stack.pop())
      stack.append(o)

  while(stack):
    postfix.append(stack.pop())
  
  return postfix


postfix = ''.join(itop(infix))
print(postfix)