import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [3, 4, 1, 7, 5]
z = [200, 400, 100, 100, 500]
titulo = "Scatter Graphic - Plot Nº 2"
eixox = "$x$"
eixoy = "$f(x)$"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.scatter(x, y, label = "My Points", color = "#990000", marker = ".", s = z)
plt.plot(x, y, color = "#009999", linestyle = "-")
plt.legend()
plt.show()