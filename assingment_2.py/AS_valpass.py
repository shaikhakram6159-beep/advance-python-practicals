import re
pass1=input("enter pass:-")
p=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_]).{8,}$"
if re.match(p,pass1):
    print("valid password")
else:
    print("invalid password")