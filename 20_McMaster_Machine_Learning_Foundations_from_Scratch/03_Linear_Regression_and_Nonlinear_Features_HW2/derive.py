import numpy as np
import matplotlib.pyplot as plt

phis = np.linspace(-1, 1, 100)
f = lambda phi: (1+phi)/((1-phi)*10)

plt.plot(phis, f(phis))
plt.ylim(-10, 10)
plt.title('Plot of f(φ) = (1+φ)/(1-φ)')
plt.xlabel('φ')
plt.ylabel('f(φ)')
plt.grid()
plt.xlim(-1, 1)
plt.ylim(-100, 100)
plt.show()