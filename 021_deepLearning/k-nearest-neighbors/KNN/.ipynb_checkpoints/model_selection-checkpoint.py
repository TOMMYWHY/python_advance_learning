import numpy as np


def train_test_split(X, y, test_ratio=0.2, seed=None):
    assert X.shape[0] == y.shape[0], "X and y not match"
    assert 0.0 <= test_ratio <= 1.0, "test_ratio is invalid"

    if seed:
        np.random.seed(seed)

    shaffle_indexes = np.random.permutation(len(X))  # 随机 排序 150
    test_size = int(len(X) * test_ratio)  # 测试数据集 大小
    test_indexes = shaffle_indexes[:test_size]
    train_indexes = shaffle_indexes[test_size:]

    X_train = X[train_indexes]  # 训练集
    y_train = y[train_indexes]  #

    X_test = X[test_indexes]  # 测试集
    y_test = y[test_indexes]

    return X_train, y_train, X_test, y_test
