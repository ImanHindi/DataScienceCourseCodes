
import re
#'a' followed by 0 or more b


p=r'\b[A-Z]{1}[a-z]+'

s='Aabbbbb Aabc abC aaa0 aaadf aaaAaaab'

print(re.findall(p,s))