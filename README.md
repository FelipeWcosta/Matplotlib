# Repositório de Estudo: Matplotlib
## Resolvendo dependências
Para installar a biblioteca `matplotlib` basta utilizar o comando:
```
    py -m pip install matplotlib
```
## Criando gráficos de barras
* Criando um gráfico de barras simples:

```
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
 ```
 * *Output*
 ![bar][def]

 [def]: https://github.com/FelipeWcosta/Matplotlib/blob/main/Figs/bar.png

 * Criando um gráfico de barras para comparação com legenda:
 ```
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
 ```
* *Output*:

 ![barcom][def2]

 [def2]: https://github.com/FelipeWcosta/Matplotlib/blob/main/Figs/barcomp.png

# Gráficos *scatter*
* Criando um  gráfico *scatter*:
```
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
```

* *Output*:

![scatter][def3]

[def3]: https://github.com/FelipeWcosta/Matplotlib/blob/main/Figs/scartteplot.png

* Gráfico *scatter* parte II:

```
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
```

* *Output*:

![scatterii][def4]

[def4]: https://github.com/FelipeWcosta/Matplotlib/blob/main/Figs/scatterplot2.png

# Salvando plots
* Salvando uma figura:
```
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
```