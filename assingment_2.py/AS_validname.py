import re
name=input("enter your name->")
p=r"[A-Za-z]+$"
if re.match(p,name):
    print("valid name")
else:
    print("invalid name")