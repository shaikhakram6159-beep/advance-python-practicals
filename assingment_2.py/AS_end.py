import re
s="gfcct"
ind=re.search(r'\w+$',s)
print(ind.end())