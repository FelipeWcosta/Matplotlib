import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 9]
titulo = "Bar Graphic"
eixox = "$x$"
eixoy = "$y$"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x, y)
plt.show()
