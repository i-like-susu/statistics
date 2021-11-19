from collections import Counter


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
