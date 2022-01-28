def logSort(arr):
  dig = []
  let = []
  
  for i in arr:
    if 'dig' in i.split()[0]:
      dig.append(i)
    else:
      let.append(i)
  
  let.sort(key=lambda x: (x.split()[1:], x.split()[0]))
  return let + dig
  
logSort(['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'])

print(type(1) == int)