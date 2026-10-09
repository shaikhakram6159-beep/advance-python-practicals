def dec(f):
    def a():
        print("1")
        f()
        print("2")
    return a
@dec
def b():
    print("hello")
    b()