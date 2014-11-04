__author__ = 'neuralyang'
import numpy as np
import scipy as sp
import csv as csv
import pandas as pd


def find_mistake2(data, w):
    for i in range(0, data[:, 0].size):
        x = np.hstack((1, data[i, 0:4]))
        sign = np.sign(np.vdot(w, x))
        if sign == 0: sign = - 1
        if sign != data[i, 4]:
            return i
    return i + 1


def find_mistake(data, w, myRange):
    for i in myRange:
        x = np.hstack((1, data[i, 0:4]))
        sign = np.sign(np.vdot(w, x))
        if sign == 0: sign = - 1
        if sign != data[i, 4]:
            return i
    return data[:, 1].size


def correct_mistake(data, w, i):
    global _count
    _count += 1
    x = np.hstack((1, data[i, 0:4]))
    return w + 0.5 * np.dot(data[i, 4], np.reshape(x, [5, 1]))


def update(data):
    w = np.zeros([5, 1])
    i = 0
    while i < data[:, 0].size:
        w = correct_mistake(data, w, i)
        i = find_mistake2(data, w)


def pocket_find_mistake(data, w):
    mistakes = []
    for i in range(0, data[:, 0].size):
        x = np.hstack((1, data[i, 0:4]))
        sign = np.sign(np.vdot(w, x))
        if sign == 0: sign = - 1
        if sign != data[i, 4]:
            mistakes.append(i)
    return mistakes


def pocket_correct_mistake(data, w, mistakes):
    np.random.shuffle(mistakes)
    i = mistakes[0]
    return correct_mistake(data, w, i)


def q16(data):
    global _count
    sum = 0
    for j in range(0, 2000):
        w = np.zeros([5, 1])
        i = 0
        # np.random.seed = np.random.randomint(0, 32291)
        myRange = range(0, data[:, 0].size)
        np.random.shuffle(myRange)
        _count = 0
        while i < data[:, 0].size:
            w = correct_mistake(data, w, i)
            i = find_mistake(data, w, myRange)
        sum += _count
    print sum / 2000


def q18(train_data, test_data):
    correct_rate = 0
    for j in range(0, 2000):
        # training
        w_hat = w = np.zeros([5, 1])
        least_mis = train_data[:, 0].size
        for i in range(0, 50):
            mistakes = pocket_find_mistake(train_data, w)
            if len(mistakes) < least_mis:
                w_hat = w
                least_mis = len(mistakes)
            if not mistakes:
                break
            w = pocket_correct_mistake(train_data, w, mistakes)
        # testing
        test_mistakes = pocket_find_mistake(test_data, w_hat)
        correct_rate += float(len(test_mistakes)) / test_data[:, 0].size
    print(correct_rate / 2000)


if __name__ == "__main__":
    global _count
    _count = 0
    # data = np.loadtxt('Data/hw1_15_train.dat')
    # q16(data)
    train_data = np.loadtxt('Data/hw1_18_train.dat')
    test_data = np.loadtxt("Data/hw1_18_test.dat")
    q18(train_data, test_data)
    # print _count