import numpy as np
from sklearn.metrics import accuracy_score


class LogisticRegression:
    def __init__(self):
        self.coef_ = None  # coefficient 系数
        self.interception_ = None  # interception 截距
        self._theta = None

    def _sigmoid(self,t):
        return 1 / (1 + np.exp(-t))



    def __repr__(self):
        return "Logistic regression"

    def fit(self, X_train, y_train, eta=0.01, n_iters=1e4):
        def J(theta, X_b, y):
            y_hat = self._sigmoid(X_b.dot(theta))
            try:
                return -np.sum(y*np.log(y_hat) + (1-y)*np.log(1-y_hat)) / len(y)
            except:
                return float("inf")


        def dJ(theta, X_b, y):
            return X_b.T.dot(self._sigmoid(X_b.dot(theta)) - y)  / len(X_b)

        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e3, epsilon=1e-8):
            theta = initial_theta
            cur_iter = 0
            while cur_iter < n_iters:
                gradient = dJ(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient
                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break
                cur_iter += 1
            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b, y_train, initial_theta, eta, n_iters)
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self

    def predict_proba(self, X_predict):
        # assert.....
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return self._sigmoid(X_b.dot(self._theta) )

    def predict(self, X_predict):
        # assert.....
        proba = self.predict_proba(X_predict)
        return np.array(proba>=0.5,dtype="int")

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        score = accuracy_score(y_test,y_predict)
        return score
