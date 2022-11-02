# Ejercicio 9.5: Setear el color de un scatter plot
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize = (8, 6), dpi = 80)

ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])

n = 3000
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan(np.abs(X)/np.abs(Y))
plt.scatter(X, Y, alpha = 0.3, c = T, cmap = 'viridis')
plt.xlim(-1, 1)
plt.ylim(-1, 1)