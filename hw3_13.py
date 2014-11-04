__author__ = 'neuralyang'

import random
import numpy as np
from sklearn import linear_model


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def f(x):
    return sign(x[0] ** 2 + x[1] ** 2 - 0.6)


def genX(N=1000):
    return np.array([np.array([random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]) for i in xrange(N)])


def addNoise(Y):
    ret = Y[:]
    for i in range(len(Y)):
        if random.random() < 0.1:
            ret[i] *= -1
    return ret

def transform(x):
    return np.array([x[0], x[1], x[0]*x[1], x[0]**2, x[1]**2])


def genXY(N = 1000):
    X = genX()
    Y = addNoise(map(f, X))
    return X, Y


def run_q13_once(t=0):
    X_train, Y_train = genXY()

    reg = linear_model.LinearRegression()

    reg.fit(X_train, Y_train)

    predict_Y = np.array(map(sign, reg.predict(X_train)))
    E_in = sum(predict_Y != np.array(Y_train))

    return float(E_in)/len(X_train)

def run_q14():

    X_train, Y_train = genXY()
    X_train_trans = map(transform, X_train)
    reg = linear_model.LinearRegression()
    reg.fit(X_train_trans, Y_train)
    res = np.array(reg.coef_, reg.intercept_)
    return res

def run_q15_once(t=0):
     X_train, Y_train = genXY()
     X_test, Y_test = genXY()
     X_train = map(transform, X_train)
     X_test = map(transform, X_test)
     reg = linear_model.LinearRegression()
     reg.fit(X_train, Y_train)
     predict_X = np.array(map(sign, reg.predict(X_test)))
     E_out = sum(predict_X != np.array(Y_test))
     return float(E_out)/len(X_test)




#print 'q13 E_in= %.3f'% (sum([run_q13_once(i) for i in xrange(1000)])/1000.0)
#print 'q14 coef=',(np.sum([run_q14() for i in xrange(100)], axis=0)/100.0)

print 'q15 E_out=',sum([run_q15_once(i) for i in xrange(1000)])/1000.0


