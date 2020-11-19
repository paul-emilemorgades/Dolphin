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

