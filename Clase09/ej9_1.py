# ejercicio 9.1

import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1)
plt.plot([0,1,2,3],[0,1,0,1])
#plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4)
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot([0,1],[0,0])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6)
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()
