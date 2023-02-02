import matplotlib.pyplot as plt


x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Primeiro Gráfico', fontdict = {'fontname': 'Times New Roman', 'fontsize': 20})
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10, 12])
plt.show()