f = open('./계란으로 계란치기.txt')

ip = f.readline

n = int(ip())

#[내구도, 무게], 부딪히면 상대 계란의 무게만큼 내구도가 감소
eggs = [list(map(int, ip().split())) for _ in range(n)]
length = len(eggs)

answer = 0 
def dfs(i, eggs):
  global answer
  if(i == length):
    answer = max(answer, sum(s[0] <= 0 for s in eggs))
    return
  
  [crntS, crntW] = eggs[i]
  if(crntS <= 0):
    dfs(i+1, eggs)
    return
  
  allBroken = 1
  for j in range(length):
    if(j== i and eggs[j][0] < 0): continue
    
    allBroken = 0
    [s, w] = eggs[j]
    
    eggs[i] = [crntS-w, crntW]
    eggs[j] = [s-crntW, w]
    dfs(i+1, eggs)
    eggs[i] = [crntS, crntW]
    eggs[j] = [s, w]

  if(allBroken):
    dfs(length, eggs)
dfs(0, eggs)

print(answer)