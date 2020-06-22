import math
def myF(an):
    return an * (1 - an)
def myF2(an):
    return math.sin(an)
def myEx39(a0,N):
    sum1 = (0.5 * (a0 + math.sqrt(a0**2 - 4)))**(2**N)
    sum2 = (0.5 * (a0 - math.sqrt(a0**2 - 4)))**(2**N)
    return sum1 + sum2

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

def ex39(a0, N):
    arr = list()
    arr.append(a0)
    for i in range(0,N):
        print(i,end = "    ")
    print()
    print(a0,end = "    ")
    for i in range(1,N):
        a = myEx39(a0,i)
        arr.append(a)
        print(a, end = "    ")
    print()

    print(arr)

    # # for latex
    for i in range(1,N):
        print("{0:3d} & {1:6.4f}\\\\".format(i,arr[i]))


def problem(N):
    a0 = a1 = a2 = 0
    An = [None] * (N + 1)
    Bn = [None] * (N + 1)
    An[0] = An[1] = An[2] = 0
    Bn[0] = Bn[1] = Bn[2] = 0
    for i in range(3, N+1):
        An[i] = (i-3)/i * An[i-1] + 1
        Bn[i] = (i+1)/4
    if (N < 100):
        for i in range(3,N + 1):
            print("{0:3d} & {1:6.4f} & {2:6.4f}\\\\".format(i,An[i],Bn[i]))
    else:
        print(An[N], Bn[N])
problem(999)