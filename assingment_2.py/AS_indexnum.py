import re
s="gfcct"
m=re.search(r"\w+$",s)
print(m.start())