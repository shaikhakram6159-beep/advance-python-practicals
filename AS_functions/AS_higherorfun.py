def cube(n):
    return n**3
def higher_order(func,num):
    return func(num)
num=int(input("enter any number:"))
result=higher_order(cube,num)
print("cube of the number is :- ",result)