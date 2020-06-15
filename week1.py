import numpy as np
import matplotlib.pyplot as plt
def smallFunc(m):
    return 2/3 * float(m) * (m - 1)/(m+2) - 2 * np.log(m + 2)
M = list(range(10))
print(M)
fM = list(map(smallFunc, M))
print(fM)
plt.plot(M,fM)
plt.xticks(M)
plt.xlabel('M')
plt.ylabel('f(M)')
plt.title('plot of f(M)')
nameFile = "./fM.png"
plt.savefig(nameFile)
plt.show()