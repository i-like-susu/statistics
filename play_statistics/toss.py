import matplotlib.pyplot as plt
import random


# 模拟抛硬币
def toss_res():
    return random.randint(0, 1)

if __name__ == '__main__':

    freq = []
    indice = []
    for toss_num in range(1, 10000):
        heads = 0
        for _ in range(toss_num):
            if toss_res() == 0:
                heads += 1
        freq.append(heads/toss_num)
        indice.append(toss_num)

    plt.plot(indice, freq)
    plt.show()
