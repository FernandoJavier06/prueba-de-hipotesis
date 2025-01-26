import matplotlib.pyplot as plt

# Crear una gráfica simple
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 3, 5]
plt.plot(x, y, label="Mi Gráfica")

# Agregar una leyenda sin marco
plt.legend(frameon=False)

# Mostrar la gráfica
plt.show()