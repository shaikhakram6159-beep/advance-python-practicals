import re
text="maths:24,python:29,java:26,cpp:27"
p=r"python:\s*([0-9]+)"
result=re.search(p,text)
if result:
    print("python marks:",result.group(1))
else:
    print("python marks not found")
    