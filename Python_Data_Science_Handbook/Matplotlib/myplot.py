# recordar: se debe correr en Python 3.9 (del equipo)
# no en base de Jupyter
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()