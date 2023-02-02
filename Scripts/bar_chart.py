import matplotlib.pyplot as plt


labels = ['a', 'b', 'c', 'd']
values = [2, 3, 4, 6]

bars = plt.bar(labels, values)


bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')

#plt.figure(figsize=(6, 4))

plt.show()