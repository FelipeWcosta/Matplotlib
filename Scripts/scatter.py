import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 9]
titulo = "Scatterplot Graphic"
eixox = "$x$"
eixoy = "$f(x)$"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.scatter(x, y, label = "My points", color = "m", marker = "h", s = 100)
plt.plot(x, y, color = "k", linestyle = "-.")
plt.legend()
plt.show()