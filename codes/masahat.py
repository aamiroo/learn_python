
def masahat ():
    a = (int(input("enter the length: ")))
    b = (int(input("enter the width: ")))
    e = (input("s or p ? "))

    if e == "s":
        return a * b
    elif e == "p":
        return a + a + b + b
    else:
        print("not available")
    return
start = masahat()
print(start)