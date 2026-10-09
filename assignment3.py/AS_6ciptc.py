import itertools 
c=['red','green',"blue"]
cy=itertools.cycle(c)
for i in range(6):
    print(next(cy))

from itertools import islice
d=range(10)
r=(list(islice(d,2,8,2)))
print(r)

from itertools import pairwise
n=[1,2,3,4]
print(list (pairwise(n)))

from itertools import tee
a,b=itertools.tee(n,2)
print(list(a))
print(list(b))


from itertools import chain
l1=[1,2,3]
l2=['a','b','c']
r=chain(l1,l2)
print(list(r))