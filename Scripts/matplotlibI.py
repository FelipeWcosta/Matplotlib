import matplotlib.pyplot as plt
import numpy as np


#Resize your graph
plt.figure(figsize = (7, 4), dpi = 300)

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

x2 = np.arange(0, 4, 0.5)
plt.plot(x2[:5], x2[:5]**2, 'm--')
plt.plot(x2[4:], x2[4:]**2, 'm', label = '$x^2$')

plt.plot(x, y, label = '$2x$', color = 'green', linewidth = 1, linestyle = 'dashdot', marker = 'h', markersize = 10, markeredgecolor = 'blue')
plt.title('Primeiro Gráfico', fontdict = {'fontname': 'Fira Code', 'fontsize': 20})
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10, 12])
plt.legend()
plt.savefig('my_graph.png', dpi = 300)
plt.show()