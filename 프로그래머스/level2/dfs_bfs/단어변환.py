def isOneLetterDiff(a, b):
    count = 0 
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            
    return count == 1

def solution(begin, target, words):
    answer = 100
    visited = []
    
    def dfs(crnt, count):
        nonlocal answer
        
        if crnt == target:
            answer = min(answer, count)
            return
        
        for word in words:
            if word not in visited and isOneLetterDiff(crnt, word):
                visited.append(word)
                dfs(word, count+1)
                visited.pop()
        
    dfs(begin, 0)
    if answer == 100:
        return 0
    return answer