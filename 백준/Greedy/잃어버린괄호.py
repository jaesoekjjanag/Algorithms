# 적당히 괄호를 쳐서 연산을 최소로 만들기

string = list(input().split('-'))

answer = sum(list(map(int,string[0].split('+'))))

for plus in string[1:]:
  numbers = list(map(int,plus.split('+')))
  answer -= sum(numbers)
  
print(answer)
