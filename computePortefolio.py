import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import quandl
import scipy.optimize as sco


def computeMean(tab):
    return [np.mean(i) for i in tab]

assert(computeMean([[2,2,2]])[0] == 2)

def computeMeansAndCov(listofAllReturns):
    return (computeMean(listofAllReturns),np.corrcoef(listofAllReturns))

tab1 = range(10)
tab2 = [2*i for i in tab1]
tab3 = [3,0,6,-18,20,40,51,16,0,1]
tab4 = [3,1,4,1,5,3,6,8,4,3]
tab = [tab1,tab2,tab3,tab4]

assert(computeMeansAndCov(tab)[0][0] == 4.5)
assert(computeMeansAndCov(tab)[1][2][2] == 1)

def computeStandardDeviation(weights, cov):
    return  np.sqrt(np.dot(weights.T, np.dot(cov, weights)))

weights = np.array([1,1])
cov = [[1,1],[1,1]]

assert(computeStandardDeviation(weights,cov) == 2.)

def computeReturns(weights, means):
    return np.dot(weights.T,means)

def computeSharp(means, cov, weights):
    nom = computeReturns(weights,means) - 0.05
    return nom/computeStandardDeviation(weights,cov)

assert(computeSharp(weights,cov,np.array([0.5,0.5])) == 0.95)

def getTheNBest(means,n):
    tab = [0 for i in range(len(means))]
    for i in range(len(means)):
        tab[i] = (i, means[i])
    res = sorted(tab, key = lambda item: item[1], reverse=True)
    res = res[:n]
    return [i[0] for i in res]

assert(getTheNBest([1,2,-44,1000],4) == [3, 1, 0, 2])

assert(getTheNBest([1,2,-44,1000],2) == [3, 1])

