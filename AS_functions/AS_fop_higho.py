def check_result(marks):
    return "pass" if marks>=40 else "fail"

def apply_check(func,m):
    return func(m)

marks=int(input("enter your marks:-"))
result=apply_check(check_result,marks)
print("your result is :-",result)