f = open('문서검색.txt')

doc = f.readline().rstrip()
word = f.readline().rstrip()

count = 0

wLen = len(word)
sub = len(doc) - wLen

i = 0
while(i < sub):
  if doc[i] != word[0]:
    i += 1

  elif(doc[i:i+wLen] == word):
    count += 1
    i += wLen

print(count)