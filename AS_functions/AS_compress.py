import itertools
s="GFFCT"
selectors=[True,True,True,False,False]
result=itertools.compress(s,selectors)
print("result:-",list(result))