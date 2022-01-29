from typing import Counter
import re

def mostCommon(paragraph, banned):
  words = [word  for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
  return Counter(words).most_common(1)[0][0]
  
  
  
paragraph = "Bob hit a ball, the git BALL flew far after it was hit"
banned = ['hit']
mostCommon(paragraph, banned)