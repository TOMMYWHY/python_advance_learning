import  numpy as np
from sklearn.metrics import mean_squared_error

class LinearRegression:
    def __init__(self):
        self.coef_ = None      # coefficient 系数
        self.interception_ = None  # interception 截距
        self._theta = None

    def fit_normal(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0], "size not match~!"
        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)
        self.interception_ = self._theta[0]
        self.coef_ =self._theta[1:]
        return self

    def predict(self, X_predict):
        # assert.....
        X_b = np.hstack([np.ones((len(X_predict),1)),X_predict])
        return  X_b.dot(self._theta)

    def score(self,X_test, y_test):
        y_predict = self.predict(X_test)
        score = 1 - mean_squared_error(y_test, y_predict) / np.var(y_test)  # var 方差
        return score

    def __repr__(self):
        return "linear regression"
