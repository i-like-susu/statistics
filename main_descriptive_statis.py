from collections import Counter
from play_statistics.descriptive_statis import frequency, mode, median, mean, rng, quartile, variance, std

if __name__ == '__main__':
    # 测试频数
    data = [2, 1, 3, 4, 5, 8]
    counter = Counter(data)
    print(counter.most_common())

    # 测试频率
    print(frequency(data))

    # 测试众数
    mode, count = mode(data)
    print(mode)
    print(count)

    # 测试中位数
    median = median(data)
    print(median)

    # 测试均值
    mean = mean(data)
    print(mean)

    # 极差
    print(rng(data))

    # 四分位数
    q1, q2, q3 = quartile(data)
    print(q1, q2, q3)

    # 方差
    variance = variance(data)
    print(variance)

    # 标准差
    print(std(data))
