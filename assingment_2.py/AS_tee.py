import itertools
clg_n=["gfcct"]
a,s,d,f,e=itertools.tee(clg_n,5)
print (list(a))
print(list(s))
print(list(d))
print(list(f))
print(list(e))