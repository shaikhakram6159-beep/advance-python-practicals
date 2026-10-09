import re
s="my college name is GFCCT"
m=re.search(r"\w+$",s)
print(m.group())