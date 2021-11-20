import matplotlib.pyplot as plt
import random
from collections import Counter

if __name__ == '__main__':
# scatter plot
# random.seed(666)
# x = [random.randint(0, 100) for i in range(100)]
# y = [random.randint(0, 100) for i in range(100)]
# plt.scatter(x, y)
# plt.show()

# line plot
# x = [random.randint(0, 100) for i in range(100)]
# plt.plot([i for i in range(100)], x)
# plt.show()

# bar plot
# data = [2, 1, 3, 1, 2, 5, 3, 4, 2, 1, 5, 2, 4]
# counter = Counter(data)
# res = counter.most_common()
# x = [point[0] for point in res]
# y = [point[1] for point in res]
# plt.bar(x, y)
# plt.show()

# histogram plot
# data = [random.randint(0, 100) for i in range(100)]
# plt.hist(data, rwidth=0.8, bins=5, density=True)
# plt.show()

# boxplot
# data = [random.randint(0, 100) for i in range(100)]
# data.append(-200)
# data.append(200)
# plt.boxplot(data)
# plt.show()

# boxplot_2
    data1 = [random.randint(0, 60) for i in range(100)]
    data2 = [random.randint(40, 100) for i in range(100)]
    plt.boxplot([data1, data2])
    plt.show()
