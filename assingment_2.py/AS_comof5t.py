#6
import itertools
t5=[x*5 for x in range (1,11)]
c=itertools.combinations(t5,5)
print(list(c))