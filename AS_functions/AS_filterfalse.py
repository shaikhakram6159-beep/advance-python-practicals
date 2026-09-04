import itertools
num=[10,20,30,40,50,60,80,100]
d=itertools.filterfalse(lambda x:x>60,num)
print ("after filterfalse :-",list(d))