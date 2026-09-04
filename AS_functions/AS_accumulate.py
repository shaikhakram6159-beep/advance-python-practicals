import itertools 
table6=[6*i for i in range(1,11)]
run_sum=itertools.accumulate(table6)
print("running addition is:-")
for i in run_sum:
    print(i)