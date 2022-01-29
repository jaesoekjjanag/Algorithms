def longestPalindrome(s):
  length = len(s)
  if length < 2 or s == s[::-1]:
    return s
  
  def detect(start, end):
    palindrome = ''
    if(start <= 0):
      start = 0
    if(end >= length-1):
      end = length-1
      
    while(start >=0 and end<=length-1):
      if(s[start] == s[end]):
        palindrome = s[start: end+1]
        start -= 1
        end += 1
      else:
        return palindrome
      
    return palindrome
  results = []
  
  for i in range(length):
    results.append(max(detect(i, i+1), detect(i-1, i+1), key=lambda x: len(x)))
    
  return max(results, key=lambda x: len(x))
    
longestPalindrome('baba')
