import itertools
sub=[("engilsh",22),("maths",26),("yoga",25),("cpp",20),("python",24)]
sub.sort(key=lambda x:x[0])

group=itertools.groupby(sub,key=lambda x:x[0])
for k,v in group:
    print(f"k={k} v{list(v)}")
