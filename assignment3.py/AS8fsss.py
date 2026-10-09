import re
m="Akki shaikh123"
d=re.findall(r"\d+",m)
print(d)



text="i like apples"
s=re.sub(r"apple","banana",text)
print(s)

text="apple,banana;cherry orange"
f=re.split(r"[;,]",text)
print(f)

t="i have 2 apples"
m=re.search(r"\d+",t)
if m:
    print(m.group())
