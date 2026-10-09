#9
def s(**k):
    print(type(k))
    for k1,v1 in k.items():
        print(f"{k1}={v1}")
s(cpp=25,python=28,maths=22,java=26,evs=29,yoga=27)
