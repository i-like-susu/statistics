from collections import Counter
from play_statistics.descriptive_statis import frequency, mode, median, mean


if __name__ == '__main__':

    #测试频数
    data = [2, 1, 3, 8]
    counter = Counter(data)
    print(counter.most_common())

    #测试频率
    print(frequency(data))

    #测试众数
    mode, count = mode(data)
    print(mode)
    print(count)

    # 测试中位数
    median = median(data)
    print(median)

    # 测试均值
    mean = mean(data)
    print(mean)