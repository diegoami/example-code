def f1(a):
    print(a)
    print(b)
#  f1(3)
b = 6
f1(3)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
     global b
     print(a)
     print(b)
     b = 9

f3(6)

def f4(b):
    def f5(a):
        nonlocal b
        print(a)
        print(b)
        b = 7
    return f5

...
f5b = f4(8)
f5b(2)