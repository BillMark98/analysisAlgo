import numpy as np
import matplotlib.pyplot as plt
N = 1500
arr = [None] * (N+1)
brr = [None] * (N+1)
crr = [None] * (N+1)
arr[1] = arr[2] = arr[3] = 1
brr[1] = brr[2] = brr[3] = 1
plotLines = []
for i in range(4, N+1):
    arr[i] = 3 * arr[i//3] + i
    brr[i] = i * np.log(i)/np.log(3)
    crr[i] = brr[i] - arr[i]

l1, = plt.plot(range(1,N+1),arr[1:])
l2, = plt.plot(range(1,N+1),brr[1:], '--')

plotLines.append([l1, l2])

legend1 = plt.legend(plotLines[0], ["a_n", "nlogn"], loc=4)
# plt.legend([l[0] for l in plotLines],loc=4)
plt.gca().add_artist(legend1)
# plt.plot(range(1,N+1),arr[1:],range(1,N+1),brr[1:])
plt.savefig("./recurrence.png")

plt.figure()
plt.plot(range(1,N + 1),crr[1:])
plt.title("difference")
plt.savefig("./difference.png")
plt.show()