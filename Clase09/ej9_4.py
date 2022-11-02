# Ejercicio 9.4: Coordenadas polares
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 6), dpi=80)
plt.axes([0, 0, 1, 1])
plt.subplot(projection = 'polar')

ax = plt.gca()
ax.set_yticklabels([])
ax.set_xticklabels([])

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)