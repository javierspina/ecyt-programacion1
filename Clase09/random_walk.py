# random_walk.py
import numpy as np
from matplotlib import pyplot as plt

def randomwalk(largo: int) -> np.ndarray:
    """
    Genera una random walk.
    Devuelve un ndarray con de los n pasos con la suma acumulada de los n pasos en n.
    """
    pasos = np.random.randint (-1, 2, largo)
    return pasos.cumsum()

def plot_randomwalks(walks:int = 8) -> None:
    plt.figure()
    plt.subplot(2, 1, 1)
    max_walk, min_walk = np.zeros(1), np.zeros(1)
    for i in range(0, walks):
        rw = randomwalk(100000)
        if rw.sum() > max_walk.sum():
            max_walk = rw
        if rw.sum() < min_walk.sum():
            min_walk = rw
        plt.plot(rw)
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Distancia al origen [metros]')

    plt.subplot(2, 2, 3)
    plt.plot(max_walk)
    plt.subplot(2, 2, 4)
    plt.plot(min_walk)
    plt.show()

plot_randomwalks()
