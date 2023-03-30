def calculate(operand, operator):
  for i in operand:
    a = int(operand.pop())
    b =int(operand.pop())
    op = operator.pop()
    if op == '+':
      operand.append(a+b)
    if op == '-':
      operand.append(a-b)
    if op == '*':
      operand.append(a*b)
    if op == '/':
      operand.append(a/b)
  return operand[0]

def postfix(p):
  operators =['+','-','*','/']
  outstack = []
  opstack =[]

  for i in p:
    if i in operators:
      if len(opstack) == 0:
        opstack.append(i)
      # 이전 연산자보다 우선순위가 높으면 opstack에 append
      elif( i in ['*', '/']) &( opstack[-1] in ['+', '-']):
        opstack.append(i)
      # 이전 연산자와 현재 연산자의 우선 순위가 같으면 
      # 이전 연산자의 우선순위가 높으면 pop. i in ['+','-'] & opstack[-1] in ['*','/']:
      # 이전 연산자가 괄호일 경우도 고려
      else:
        pop = opstack.pop()
        outstack.append(pop)
        opstack.append(i)
    # elif i == '(':
    #   opstack.append(i)
    # elif i == ')':
    #   # 왼쪽 괄호가 나올 때까지 모든 연산자 pop하고 outstack에 저장. 괄호는 저장하지 않음.
    #   print(opstack)
    #   op = ''
    #   inner =[]
    #   while op != '(':
    #     op = opstack.pop()
    #     if op not in ('(', ')'):
    #       inner.append(op)
    #   print(inner[::-1])
    else:
      outstack.append(i)

  for op in opstack:
    opstack.pop()
    outstack.append(op)

  operand = []
  operator =[]

  for isOp in outstack:
    if isOp in operators:
      operator.append(isOp)
    else:
      operand.append(isOp)

  print(operand, operator)
  return calculate(operand, operator)

print(postfix(input()))