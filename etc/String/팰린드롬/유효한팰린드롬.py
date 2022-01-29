import re

def isPalindrome(s):
  strs = re.sub('[^a-zA-Z0-9]', '',s).lower()

  lp = 0
  rp = len(strs) - 1

  while(lp < rp):
    if(strs[lp] == strs[rp]):
      lp += 1
      rp -= 1
    else:
      return False
      
  return True

      