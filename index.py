import numpy as np
import matplotlib.pyplot as plt


np.random.seed(10)
y = np.random.randint(low=1, high=1500, size=10)
print(y)

plt.plot(y)

data = np.random.normal(10, 0.5, 5000)
# plt.hist(data)
plt.boxplot(data)
plt.show()