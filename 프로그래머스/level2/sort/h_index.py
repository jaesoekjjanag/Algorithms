def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    
    for idx, c in enumerate(citations):
        h = idx + 1;
        if h == c:
            answer = c
            break;
        if h > c:
            answer = citations[idx - 1] - 1
            break;
          
    print(citations)
    return answer
  
print(solution([11, 17, 8, 9, 6, 6, 3, 4]))