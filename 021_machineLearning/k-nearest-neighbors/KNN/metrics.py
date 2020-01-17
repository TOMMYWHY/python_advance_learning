import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def accuracy_score(y_true, y_predict):
    assert y_true.shape[0] == y_predict.shape[0], "not match"
    return sum(y_predict == y_true) / len(y_true)


def r2_score(y_true, y_predict):
    return 1- mean_squared_error(y_true,y_predict) / np.var(y_true)
