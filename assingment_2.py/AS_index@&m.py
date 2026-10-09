import re
mail="shaikh1234@gmail.com"
p=re.search(r"\@",mail)
print(p.start())
p1=re.search(r"m$",mail)
print(p1.start())