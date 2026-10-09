import re
gmail="exaple123@gmail.com"
p=r"[A-Za-z0-9._]+@[0-zA-Z._]+.[a-zA-z]{2}$"
if re.match(p,gmail):
    print("valid gmail")
else:
    print("invalid gmail")