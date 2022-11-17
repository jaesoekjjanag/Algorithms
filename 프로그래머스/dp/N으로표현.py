# number를 최소개의 N으로 표현.
# 최솟값이 8보다 크면 -1

# dp: N을 해당 index만큼 사용하여 만들 수 있는 모든 수  
# dp[1] 

def solution(N, number):
    dp = [0] + [set([int(str(N)*i)]) for i in range(1, 9)] # 1부터 8까지. 0번 index가 1, 7번 index가 8
    
    for i in range(1, 9):
      # a + b = i
      for j in range(1, i):
        k = i - j
        for a in dp[j]:
          for b in dp[k]:
            dp[i].add(a+b)
            dp[i].add(abs(a-b))
            dp[i].add(a*b)
            if b != 0:
              dp[i].add(int(a//b))
      
      if number in dp[i]:
        return i

        
solution(5, 12)
solution(2, 11)