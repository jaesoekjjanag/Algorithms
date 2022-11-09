from collections import defaultdict 

def solution(clothes):      
    dict = defaultdict(list)
    cats= []
    
    for cloth, cat in clothes:
        dict[cat].append(cloth)
        cats.append(cat)
        
    length = len(dict)
    
    def dfs(index, s, result):
      if(len(s) == length):
          sum = 1
          for i in range(length):
            sum *= max(len(dict[cats[i]]) * int(s[i]), 1)
          if(s != '0'*length):
            # print(s, sum, result)
            return sum 
          else:
            return 0
      
      a = dfs(index + 1, s + '0', result)
      b = dfs(index + 1, s + '1', result)
      
      return result + a + b
    
    print(dfs(0, '', 0))


solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])