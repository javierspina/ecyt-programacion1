# random_walk.py
import numpy as np
from matplotlib import pyplot as plt

def randomwalk(largo: int) -> np.ndarray:
    """
    Genera una random walk.
<<<<<<< Updated upstream
    Devuelve un ndarray con de los n pasos
    con la suma acumulada de los n pasos en n.
=======
    Devuelve un ndarray con de los n pasos con la suma acumulada de los n pasos en n.
>>>>>>> Stashed changes
    """
    pasos = np.random.randint (-1, 2, largo)
    return pasos.cumsum()

<<<<<<< Updated upstream
def plot_randomwalks(n_rw:int = 12,
                     largo_rw:int = 100000,
                     amplitud_y:int = 1000,
                     yticklabel:int = 500) -> None:
    """
    Grafica un número n_rw de randomwalks, individualizando la que más se 
    alejó y la que menos se alejó.
    Params:
        n_rw (int) = La cantidad de randomwalks a graficar
        largo_rw (int) = El largo de las randomwalks
        amplitud_y (int) = Amplitud del eje y
        yticklabel (int) = Marcadores para y. Debe ser menor que amplitud_y
    """
    assert amplitud_y > yticklabel, 'Amplitud debe ser mayor que el label.'
    
    # Crear figura
    plt.figure(figsize=(16, 9), dpi=120)
    
    # Crear las 12 random walks
    walks = [(randomwalk(largo_rw), i) for i in range(0, n_rw)]
    
    # Identificar más y menos se aleja
    last_steps = [(np.abs(w[0][-1]), w[0], w[1]) for w in walks]
    max_walk = max(last_steps)
    min_walk = min(last_steps)
    
    # Plot con las 12 random walks
    ax_walks = plt.subplot(2, 1, 1)
    plt.ylim(-amplitud_y, amplitud_y)
    ax_walks.title.set_text('12 caminatas al azar')
    ax_walks.set_xticks([])
    ax_walks.set_yticks([-yticklabel, 0, yticklabel])
    for w in walks:
        plt.plot(w[0])
    
    # Graficar más se aleja
    ax_maxw = plt.subplot(2, 2, 3)
    plt.ylim(-amplitud_y, amplitud_y)
    ax_maxw.title.set_text('La caminata que más se aleja')
    ax_maxw.set_xticks([])
    ax_maxw.set_yticks([-yticklabel, 0, yticklabel])
    plt.plot(max_walk[1], c = ax_walks.get_lines()[max_walk[2]].get_color())
    
    # Graficar menos se aleja
    ax_minw = plt.subplot(2, 2, 4)
    plt.ylim(-amplitud_y, amplitud_y)
    ax_minw.title.set_text('La caminata que menos se aleja')
    ax_minw.set_xticks([])
    ax_minw.set_yticks([])
    plt.plot(min_walk[1], c = ax_walks.get_lines()[min_walk[2]].get_color())
    
    # Mostrar
    plt.show()

plot_randomwalks()
=======
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
>>>>>>> Stashed changes
