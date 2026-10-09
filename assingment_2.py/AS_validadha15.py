#15
import re
adhar=input("enter your adhar number")
p=r"^[0-9]{12}$"
if re.match(p,adhar):
    print("valid adhar number")
else:
    print("invalid adhar number")