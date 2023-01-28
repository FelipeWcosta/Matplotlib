import matplotlib.pyplot as plt
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 8, 9]
x2 = [2, 4, 6, 8, 10]
y2 = [3, 4, 5, 2, 1]
titulo = "Bar Graphic - Comparation"
eixox = "$x$"
eixoy = "f(x)"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x1, y1, label = "Bar one")
plt.bar(x2, y2, label = "Bar two")
plt.legend()
plt.show()