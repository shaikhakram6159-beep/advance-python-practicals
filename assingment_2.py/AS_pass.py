import re
pass1=str(input("enter password:"))
a=r"^[A-Za-z0-9]{8}$"
if re.match(a,pass1):
    print("valid password")
else:
    print("invalid password")
