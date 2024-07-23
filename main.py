"""
def palindrome(param):
  while True:
    if param[0] == param[-1]:
      if len(param)>2:
        return palindrome(param[1:-1])
      elif len(param) == 2:
        return param[0] == param[-1]
      elif len(param) == 1:
        return True
      else:
        return False
    else:
      return False  

"""

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])


checkword = input("Enter a word that you want to check for palindromeness: ").strip().lower()
checkword = ''.join(checkword.split())    
if palindrome(checkword) == True:
  print("This is a palindrome")
else:
  print("This is not a palindrome")