def heron():

    a = (int (input("enter first side: ")))
    print()
    b = (int (input("enter second side: ")))
    print()
    c = (int (input("enter third side: ")))
    print()
    e = (input("s or p? "))
    s = a + b + c
    if e == "p":
        print (f" p of triangle: {s}")
    elif e == "a + b + c":
        h = (s*((s-a)*(s-b)*(s-c)))**0.5
        print(f"s of triangle: {h}")
act = heron()
print(act)
