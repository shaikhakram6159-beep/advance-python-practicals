10
import re
mobile=input("enter mobile number->")
patt=r"^[6-9][0-9]{9}$"
if re.match(patt,mobile):
    print("valid mobile number")
else:
    print("invalid mobil number")