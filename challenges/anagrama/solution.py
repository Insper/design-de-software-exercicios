import re
def anagrama(s1, s2):
  # change to Lower case and remove leading, trailing
  # and spaces in between
  temp1 = re.sub("^\\s+|\\s+$|\\s+", "", s1.lower())
  temp2 = re.sub("^\\s+|\\s+$|\\s+", "", s2.lower())
 
  if sorted(temp1) == sorted(temp2):
      return True
  else:
      return False