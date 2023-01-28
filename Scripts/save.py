import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 9]
z = [500, 500, 500, 500, 500]
titulo = "Scatterplot graphics"
eixox = "x"
eixoy = "f(x)"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.scatter(x, y, label = "My points", color = "#990000", marker = ".", s = z)
plt.plot(x, y, color = "#009999", linestyle = "-")
plt.legend()
plt.savefig("My_plot.png", dpi = 1200)