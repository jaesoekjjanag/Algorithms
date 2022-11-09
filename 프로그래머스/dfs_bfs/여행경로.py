from collections import defaultdict

def dfs(src, dd, answer, length):
    answer.append(src)
    if len(dd[src]) == 0:
        if len(answer) == length:
            return True
        return False

    
    for idx, dest in enumerate(dd[src]):
        del dd[src][idx]
        
        if dfs(dest, dd, answer, length) == True:
            return True
        else:
            answer.pop()
            dd[src].insert(idx, dest)  

def solution(tickets):
    answer = []
    base = "ICN"
    
    dd = defaultdict(list)
    
    for src, dest in tickets:
        dd[src].append(dest)
        dd[src] = sorted(dd[src])
    
    dfs(base, dd, answer, len(tickets)+1)
    return answer
  
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))