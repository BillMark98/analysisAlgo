import math
def myF(an):
    return an * (1 - an)
def myF2(an):
    return math.sin(an)


def ex21(N):
    a0 = 1/2
    arr = list()
    arr.append(a0)
    for i in range(0, N):
        print(i,end = "    ")
    print()
    print(a0,end = "    ")
    for i in range(1,N):
        a = myF(a0)
        arr.append(a)
        a0 = a
        print(a * i, end = "    ")
    print()

    print(arr)

    # for latex
    for i in range(1,N):
        print("{0:3d} & {1:6.4f}\\\\".format(i,arr[i]*(i+2)))

def ex22(N):
    a0 = 1
    arr = list()
    arr.append(a0)
    for i in range(0, N):
        print(i,end = "    ")
    print()
    print(a0,end = "    ")
    for i in range(1,N):
        a = myF2(a0)
        arr.append(a)
        a0 = a
        print(a * math.sqrt(i)/math.sqrt(3), end = "    ")
    print()

    print(arr)

    # # for latex
    for i in range(1,N):
        print("{0:3d} & {1:6.4f}\\\\".format(i,arr[i]*math.sqrt(i)/math.sqrt(3)))

ex22(22)