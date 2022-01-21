# 더해서 타겟을 만들 수 있는 인덱스 조합. 배열의 시작 인덱스를 1로 가정. 배열은 정렬되어있음

numbers = [2,7,11,15]
target = 9

def sum_index(numbers, target):
  p1 = 0
  p2 = len(numbers)-1
  
  while (p1 < p2):
    crnt = numbers[p1] + numbers[p2]
    if(crnt == target):
      return [p1+1, p2+1]
    
    elif(crnt > target):
      p2 -= 1
      
    else:
      p1 += 1  
  
print(sum_index(numbers, target))

