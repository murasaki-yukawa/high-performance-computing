import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.time()


def func(x, r):
    return r * x * (1 - x)


x0 = 0.8    #[0, 1]
r0 = 3.5
Nr = 10000
r = np.linspace(1, 4, Nr)

N = 300
N1 = 200
X = np.full((len(r), N1), np.nan)

z = 0

for i, ri in enumerate(r):
    x = np.zeros(N)
    xi = x0

    for n in range(N):
        x[n] = xi
        xi = func(xi, ri)

    x = np.array(x)

    x = x[-N1:]
    for j in range(len(x)):    #range(min(N1, len(x)))
        X[i, j] = x[j]
    # print(f"x = {X}")


end_time = time.time()
T = end_time - start_time
print(f"{T:.6f} сек")
#0.232389 сек


plt.figure(figsize=(10, 10))
plt.rc('font', size=16)

for i in range(Nr):
    y = X[i, :]
    plt.scatter(np.full_like(y, r[i]), y, color='k', marker='o', s=0.2)

plt.ylim(0, 1)
plt.xlim(1, 4)
plt.xlabel('r')
plt.ylabel('x')

plt.title("Бифуркационная картина")

plt.tight_layout()
plt.show()


