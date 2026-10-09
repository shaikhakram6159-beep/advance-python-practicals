#7
class a:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    def __str__(self):
        return f"your total marks of 1st year is {self.n+o.n}"
    def __add__(self,o):
        return self.n+o.n 
    def __len__(self):
        return len(str(self,m))
    def __repr__(self):
        return f"{self.m}{self.n}"
o=a("1st sem",80)
o2=a("2nd sem",80)
print(o)
print(o2)
print(repr(o2))