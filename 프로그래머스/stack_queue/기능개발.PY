from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
              
        count = 0
        
        while(progresses and progresses[0] >= 100):
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count:            
            answer.append(count)
    
    return answer
  
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))