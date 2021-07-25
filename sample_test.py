import random
from collections import Counter

import numpy as np

p_array = np.arange(1, 10)
plist = [round(float(x) / p_array.sum(), 3) for x in p_array]  ## 概率列表
print(p_array)
print(plist)

Psample = []
N = 100  ##抽样次数
n = len(plist)

index = int(random.random() * n)
mw = max(plist)
beta = 0.0

for i in range(N):  ##核心算法
    beta = beta + random.random() * 2.0 * mw
    while beta > plist[index]:
        beta = beta - plist[index]
        index = (index + 1) % n
    Psample.append(plist[index])

cresult = Counter(Psample)
psam = [cresult[x] for x in plist]
pe = [x * N for x in plist]

print(psam)

print(pe)
print([round(psam[i] / pe[i], 3) for i in range(n)])


def sample(n_val, k, prob):
    '''
    :param n_val: n个数值
    :param k:     返回k个
    :param prob:  n个值的概率

    遍历每个概率值，换算数量：1000*数量*概率值，以此重构采样空间
    '''
    import random
    sample_list = []

    for i in range(len(prob)):
        num = np.ceil(1000 * len(prob) * prob[i])
        sample_list.extend([n_val] * num)

    random.shuffle(sample_list)
    return sample_list[:k]
