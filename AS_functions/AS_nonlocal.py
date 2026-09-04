def outer():
    msg="hello"
    def inner():
        nonlocal msg
        msg="gfcct"
        print(msg)
        inner()
outer()
