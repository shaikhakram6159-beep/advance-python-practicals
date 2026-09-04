import itertools
t5=[i*5 for i in range(1,11)]
result=itertools.takewhile(lambda x:x<15,t5)
print("taken values:- ",list(result))