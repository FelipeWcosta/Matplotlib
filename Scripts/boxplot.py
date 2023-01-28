import matplotlib.pyplot as plt
import random
array = []
for i in range(10000):
    num_ran = random.randint(0, 1000000)
    array.append(num_ran)
plt.boxplot(array)
plt.show()