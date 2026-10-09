l=[1,2,3,4,5]
#performing filter function:-
e=list(filter(lambda x:x%2==0,l))
print(e)

#performing map function:-
double=list(map(lambda x:x*2,l))
print("result",double)

#performing reduce:-
from functools import reduce
r=reduce(lambda x,y:x*y,l)
print(r)