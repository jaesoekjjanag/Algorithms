def solution(numbers):
    return str(int(''.join(sorted([str(i) for i in numbers], key=lambda x: x*3, reverse=True))))
  
# 삽입 정렬을 활용한 풀이
def insert_sort(numbers):
  def toSwap(a, b):
    return str(a) + str(b) > str(b) + str(a)
  
  for i in range(1, len(numbers)):
    temp = numbers[i]
    for j in range(i-1, -1, -1):
      if toSwap(temp, numbers[j]):
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
      else:
        break
      
  return str(int(''.join(map(str, numbers))))

numbers = [3, 30, 34, 5, 9]
print(insert_sort(numbers))