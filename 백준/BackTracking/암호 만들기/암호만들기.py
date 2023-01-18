f = open('./암호만들기.txt')

ip = f.readline

L, C = map(int, ip().split())

alph = sorted(list(ip().split()))
vowels =['a', 'e', 'i', 'o', 'u']

def dfs(i, acc, v, c):
  if(len(acc) > L):
    return
  
  if(len(acc) == L and v >= 1 and c >= 2):
    print(acc)
    
  for j in range(i+1, C):
    isVowel = 0
    if(alph[j] in vowels):
        isVowel = 1
        
    dfs(j, acc+alph[j], v+isVowel, c+(1-isVowel))

for i in range(C-L+1):
  isVowel = 0
  if(alph[i] in vowels):
      isVowel = 1
        
  dfs(i, alph[i], isVowel, 1-isVowel)