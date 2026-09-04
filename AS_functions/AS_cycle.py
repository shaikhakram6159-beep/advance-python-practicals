import itertools
streams=['CS','STAT','PHY']
cycle=itertools.cycle(streams)
print("cycle streams (3 times) is:- ")
for i in range(9):
    print(next(cycle))
