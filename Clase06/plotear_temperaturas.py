'''
plotear_temperaturas.py
Autor: Javier Spina
Septiembre 2022
'''
import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas(temperaturas):
    data = np.load(temperaturas)
    plt.hist(data, bins=50)
    plt.show()

plotear_temperaturas('../Data/temperaturas.npy')
