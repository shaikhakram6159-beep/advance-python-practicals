import itertools
def add(a,b,c,d,e):
    return a+b+c+d+e
data=[(1,2,3,4,5,),(1,0,2,0,3),(6,7,8,9,0)]
result=itertools.starmap(add,data)
print("sum of each tuple is:-",list(result))#34