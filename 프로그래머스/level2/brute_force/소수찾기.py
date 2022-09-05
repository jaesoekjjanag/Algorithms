import math
from itertools import permutations

def getPrimeNumbers(max_num):
    if max_num < 2:
        return []
    
    nums = [1] * (max_num + 1)
    
    for i in range(2, int(math.sqrt(max_num))+1):
        if nums[i]:
            for j in range(2*i, max_num+1 , i):
                nums[j] = 0 
    
    nums[0], nums[1] = 0, 0

    return nums

def solution(numbers):
    answer = 0
    # 1. 만들 수 있는 가장 큰 수 찾기
    max_num = int(''.join(sorted(numbers, reverse=True)))
    
    # 2. 가능한 모든 소수 찾기
    prime_nums = getPrimeNumbers(max_num)
    
    # 3. numbers로 만들 수 있는 모든 숫자 조합 순회
    lst = set()
    
    for i in range(1, len(numbers)+1):
        for j in set(permutations(numbers, i)):
            lst.add(int(''.join(j)))
            
    for l in lst:
        if prime_nums[l]:
            answer += 1
    
    return answer