n = int(input())

pattern = []

for i in range(n):
  file = list(input())
  if i == 0:
    pattern = file
    
  for i in range(len(file)):
    if file[i] != pattern[i] and pattern[i] != '?':
      pattern[i] = '?'
  
print(''.join(pattern))