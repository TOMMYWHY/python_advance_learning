import numpy as np
from math import sqrt
from collections import Counter


def kNN_classify(k, X_train, Y_train, x):
    # 验证参数
    assert 1 <= k <= X_train.shape[0], "k is invalid"  # k 不能超出 训练集 个数
    assert X_train.shape[0] == Y_train.shape[0], " train data set invalid"  # 训练集 有效
    assert X_train.shape[1] == x.shape[0], "feature number invalid"  # 特征向量 有效

    # 算法
    distances = [sqrt(np.sum((x_tr - x) ** 2)) for x_tr in X_train]  # 列表生成式
    nearest = np.argsort(distances)
    topK_y = [Y_train[i] for i in nearest[:k]]  # 前 k 个元素的 y 值
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]
