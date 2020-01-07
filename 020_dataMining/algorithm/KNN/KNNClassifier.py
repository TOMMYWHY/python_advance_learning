import numpy as np
from math import sqrt
from collections import Counter
from .metrics import accuracy_score

class KNNClassifier:
    def __init__(self,k):
        assert 1 <= k, "k is invalid"  # k 不能小于1
        self.k = k
        self._X_train = None
        self._y_train = None
    def fit(self,X_train,y_train):
        """ 用户传入 x y 训练集， 并返回 """
        assert X_train.shape[0] == y_train.shape[0], " train data set invalid"
        assert self.k <= X_train.shape[0], "k is invalid"

        self._X_train = X_train
        self._y_train = y_train
        return self

    def predict(self,X_predict):
        """ 传入需要预测的矩阵 """
        assert self._X_train is not None and self._y_train is not None,"data set is none!"
        assert self._X_train.shape[1] == X_predict.shape[1], "feature number invalid"  # 特征向量 有效
        y_predict =[self._predict(x) for x in X_predict]
        return np.array(y_predict)

    def _predict(self,x):
        assert self._X_train.shape[1] == x.shape[0], "feature number invalid"  # 特征向量 有效
        distances = [sqrt(np.sum((x_tr - x) ** 2)) for x_tr in self._X_train]  # 列表生成式
        nearest = np.argsort(distances)
        topK_y = [self._y_train[i] for i in nearest[:self.k]]  # 前 k 个元素的 y 值
        votes = Counter(topK_y)
        return votes.most_common(1)[0][0]

    def score(self,X_test,y_test):
        """准确度"""
        y_predict = self.predict(X_test)
        return accuracy_score(y_test,y_predict)

    def __repr__(self):
        return "KNN(k=%d)" % self.k
