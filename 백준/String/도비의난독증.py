f = open("도비의난독증.txt")

while(True):
  n = int(f.readline().rstrip())
  if not n:
    break
  
  words = [[f.readline().rstrip()] for _ in range(n)]
  for i in words:
    i.append(i[0].lower())
    i.reverse()
    
  words.sort()
  print(words[0][1])