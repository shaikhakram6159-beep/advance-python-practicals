r=0
def m(*a):
    global r
    print(type(a))
    for i in a:
        r=r+i
    return r
print(m(21,23,24,25,27,28,29))
