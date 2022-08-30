def solution(prices):
    length = len(prices)
    
    answer = [0] * length 
    stack = []
    
    # 가격이 떨어지지 않은 가격들을 stack에 넣어두기
    # stack과 현재 가격을 비교해 현재 가격이 더 낮으면 stack에서 pop하고 answer[i]에 더하기
    
    for i in range(len(prices)):
        crnt = prices[i]
        
        # stack에는 항상 낮은 순서대로 입력되어있음
        while stack and crnt < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        
        if(i == length-1):
            for s in stack:
                answer[s] = i - s
        stack.append(i)

    return answer

print(solution([1, 2, 3, 2, 3]))