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

 ![barcom][def2]

 [def2]: https://github.com/FelipeWcosta/Matplotlib/blob/main/Figs/barcomp.png
