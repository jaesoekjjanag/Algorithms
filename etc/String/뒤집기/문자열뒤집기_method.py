# def reverseStr(s):
#   p = len(s)-1
#   rs = []
  
#   for i in range(p,0,-1):
#     rs.append(s[i])

#   s = rs
  
def reverseStr(s):
  left, right = 0, len(s)-1
  while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
  
reverseStr(["h", "e", "l", "l", "o"])