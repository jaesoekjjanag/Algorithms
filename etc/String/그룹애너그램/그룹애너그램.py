from collections import defaultdict

def group(words):
  ana = defaultdict(lambda: [])
  
  
  for word in words:
    ana[''.join(sorted(word))].append(word)
    
  return list(ana.values())
  
group(['eat', 'tea', 'ate', 'tan', 'nat', 'bat'])