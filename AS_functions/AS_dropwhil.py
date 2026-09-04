import itertools
num=[10,20,30,40,50,60]
d=itertools.dropwhile(lambda x:x<40,num)
print ("after droping:-",list(d))