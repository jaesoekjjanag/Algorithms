# 봄:
# - 나무는 자신의 위치한 땅에서 나이만큼 양분을 먹고 나이 1 증가
# - 여러 나무가 함께 있다면 어린 나무부터 먹는다
# - 자신의 나이만큼 먹을 수 없다면 죽는다

# 여름: 봄에 죽은 나무가 양분으로 변한다. 죽은 나무의 나이를 2로 나눈 값

# 가을: 나무의 나이가 5의 배수인 경우 인접한 8개의 칸에 나이가 1인 나무 생성

# 겨울: 로봇이 돌아다니면서 땅마다 양분 추가
from heapq import heappop, heappush
input = open('./input.txt').readline

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
max_y, max_x = len(A), len(A[0])
nourish = [[5]*max_x for _ in range(n)] 
trees = list(map(lambda x: tuple([x[2], x[0], x[1]]), [tuple(map(int, input().split())) for _ in range(m)])) #y, x, age
seasons = range(4) #0:봄, 1:여름, 2:가을, 3:겨울
dead = []

def spring(trees, nourish):
  temp = []
  dead = []
  
  while trees:
    age, y, x = heappop(trees)
    if nourish[y-1][x-1] >= age:
      nourish[y-1][x-1] -= age
      heappush(temp, (age+1, y, x)) 
    else:
      dead.append((age//2, y, x))
      
  return (temp, dead)
      
def summer(nourish, dead):
  for n, y, x in dead:
    nourish[y-1][x-1] += n
    
  dead = []
  
direction = [
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, -1],
  [0, 1],
  [1, -1],
  [1, 0],
  [1, 1]
]

def fall(trees):
  for age, y, x in trees:
    if(age%5): continue
    
    for dy, dx in direction:
      ny, nx = y+dy, x+dx
      if 1<=ny<=max_y and 1<=nx<=max_x:
        heappush(trees, (1, ny, nx))
      
def winter(nourish, A):
  for y in range(1, max_y+1):
    for x in range(1, max_x+1):
      nourish[y-1][x-1] += A[y-1][x-1]
  
for _ in range(k):
  for s in seasons:
    print()
    if(s == 0):
      trees, dead = spring(trees, nourish)
      print(trees)
    if(s == 1):
      summer(nourish, dead)
    if(s == 2):
      fall(trees)
      print(trees)
    if(s == 3):
      winter(nourish, A)
    
      
print(len(trees), trees)




