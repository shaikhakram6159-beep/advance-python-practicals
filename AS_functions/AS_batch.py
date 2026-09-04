import itertools
th_m=[45,38,42,40,47,36]
batch=itertools.batched(th_m,2)
print("theory marks after batch:- ")
for m in batch:
    print(m)