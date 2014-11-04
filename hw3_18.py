import numpy as np
import random
from numpy.linalg import norm


def process(data):
    return map(lambda x: map(float, x.split()), data)


def addone(X):
    XT = X.transpose()
    one = np.ones(len(X))
    XT = np.vstack((XT,one))
    return XT.transpose()


def toXY(data):
    array_data = np.array(data)
    dim = len(data[0])
    X = addone(array_data[:, 0:dim-1])
    Y = array_data[:, dim-1]
    return X, Y

def sign(x):
    if x>=0:
        return 1
    else:
        return -1


def h(w, x):
    return 1.0/(1.0 + np.exp(-np.dot(w, x)))


def theta(x):
    if x < -50:
        return 0
    if x > 50:
        return 1
    return 1.0/(1.0 + np.exp(-x))

def grad(w, x, y):
    return theta(np.dot(-y*w, x))*(-y*x)

def update(w, X, Y, i, rate  = 0.001):
    g = grad(w, X[i], Y[i])
    return w - rate*g

def train(X, Y, rate=0.001, T=2000):
    dim = len(X[0])
    w = np.zeros(dim)
    for t in range(T):
        if t % 100 == 0:
            print 'doing', t
        upd = np.zeros(dim)
        for i in range(len(X)):
            upd += grad(w,X[i],Y[i])
        upd /= len(X)
        w -= upd*rate
    return w


def train_sgd(X, Y, rate = 0.001, T = 2000):
    dim = len(X[0])
    w = np.zeros(dim)

    pos = 0
    for i in xrange(T):
        pos = (pos + 1) % len(X)
        w = update(w, X, Y, pos, rate)
    return w


def test(w, X,Y):
    Yhat = map(lambda x: sign(np.dot(w,x)),X)
    return float(sum(Yhat != Y)) / len(X)

raw_data_train = open('Data/hw3_train.dat').readlines()
raw_data_test = open('Data/hw3_test.dat').readlines()


X_train,Y_train = toXY(process(raw_data_train))
X_test,Y_test = toXY(process(raw_data_test))

#w_18 = train(X_train, Y_train, 0.001, 2000)
#w_19 = train(X_train, Y_train, 0.01, 2000)
w_20 = train_sgd(X_train, Y_train, 0.001, 2000)


#print test(w_18, X_test, Y_test)
#print test(w_19, X_test, Y_test)
print test(w_20, X_test, Y_test)