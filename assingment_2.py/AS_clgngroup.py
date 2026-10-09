import re
s="my college name is GFCCT"
c=re.search(r"GFCCT$",s)
print(c.group())