from collections import Counter
from math import sqrt


# 频率
def frequency(data):
    counter = Counter(data)
    res = counter.most_common()
    fre = [(i[0], i[1] / len(data)) for i in res]
    return fre


# 众数
def mode(data):
    counter = Counter(data)
    res = counter.most_common()

    if res[0][1] == 1:
        return None, None

    mode_list = []
    temp = res[0][1]
    for i in res:
        if i[1] == temp:
            mode_list.append(i[0])
        else:
            break
    return mode_list, temp


# 中位数
def median(data):
    sorted_data = sorted(data)
    n = len(data)

    if n % 2 == 1:
        return sorted_data[n // 2]

    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


# 均值
def mean(data):
    return sum(data) / len(data)


# 极差
def rng(data):
    return max(data) - min(data)


# 四分位数
def quartile(data):
    if len(data) < 4:
        return None, None, None
    data_sorted = sorted(data)
    q2 = median(data_sorted)
    if len(data) % 2 == 1:
        q1 = median(data_sorted[: len(data) // 2])
        q3 = median(data_sorted[len(data) // 2 + 1:])
    else:
        q1 = median(data_sorted[: len(data) // 2])
        q3 = median(data_sorted[len(data) // 2:])
    return q1, q2, q3


# 方差
def variance(data):
    n = len(data)
    if n <= 1:
        return None

    mean_data = mean(data)
    return sum((i - mean_data) ** 2 for i in data) / (n - 1)


# 标准差
def std(data):
    return sqrt(variance(data))
