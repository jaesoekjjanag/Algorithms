import sys
f = open('./구슬찾기.txt')
# ip=sys.stdin.readline
ip = f.readline

N, M =map(int,ip().split())

bigger_lst=[[] for _ in range(N+1)]  
smaller_lst=[[] for _ in range(N+1)] 
mid=(N+1)/2 

for i in range(M):  
    a,b=map(int,ip().split())
    bigger_lst[b].append(a)
    smaller_lst[a].append(b)

def dfs(x, arr, visited):
    if not arr[x]:
      return 1
    print(x)
    r = 0
    for i in arr[x]:
        if not visited[i]:
            visited[i]=True
            r+= dfs(x, arr, visited)
  
    return r    

answer=0
for i in range(1,N+1):
    if dfs(i, bigger_lst,[False]*(N+1)) >= mid:
      answer += 1
      continue
    
    if dfs(i, smaller_lst,[False]*(N+1))>=mid:
        answer+=1

print(answer)