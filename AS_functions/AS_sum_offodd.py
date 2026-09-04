from functools import reduce
odd_numbers=num=[i for i in range(1,11)if i%2==1]
squares=list(map(lambda z:z*z,odd_numbers))
total=reduce (lambda z,y:z+y,squares)
print("odd numbers",odd_numbers)
print("square of of odd number",squares)
print("sum of using reduce:",total)