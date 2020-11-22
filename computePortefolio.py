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
    res = [i[0] for i in res]
    otherAsset = [i for i in range(len(means))]
    for i in res:
        otherAsset.remove(i)
    return  res, otherAsset

assert(getTheNBest([1,2,-44,1000],4)[0] == [3, 1, 0, 2])
assert(getTheNBest([1,2,-44,1000],4)[1] == [])
assert(getTheNBest([1,2,-44,1000],2)[0] == [3, 1])
assert(getTheNBest([1,2,-44,1000],2)[1] == [0,2])

def normalize(listOfListOfFloat):
    minLength = len(listOfListOfFloat[0])
    for i in listOfListOfFloat:
        if len(i) < minLength:
            minLength = len(i)
    return [i[:minLength] for i in listOfListOfFloat]

assert(normalize([[0.8,0.8],[0.9],[0.1,0.5,0.6]])== [[0.8], [0.9], [0.1]])

def computeSharpFromPortfolio(portfolio, means, returns):
    portfolioMeans= [means[i] for i in portfolio]
    portfolioReturns = [returns[i] for i in portfolio]
    portfolioReturns = normalize(portfolioReturns)
    cov = np.corrcoef(np.array(portfolioReturns))
    weights =np.array( [1./len(portfolio) for i in portfolio])
    return computeSharp(portfolioMeans,cov,weights)



portfolio = [2,5,6]
returns = [[i%2,i%3,i%4] for i in range(10)] 
means = range(10)
mat = [[2%2,2%3,2%4],[5%2,5%3,5%4],[6%2,6%3,6%4]]
weights = np.array( [1./len(portfolio) for i in range(3)])
cov = np.corrcoef(mat)
portfolioMeans = [2,5,6]
assert(computeSharpFromPortfolio(portfolio,means,returns) == computeSharp(portfolioMeans,cov, weights))

portfolio = [2,5,6]
returns = [[float(i%2),float(i%3),float(i%4)] for i in range(10)] 
means = range(10)
mat = [[2%2,2%3,2%4],[5%2,5%3,5%4],[6%2,6%3,6%4]]
weights = np.array( [1./len(portfolio) for i in range(3)])
cov = np.corrcoef(mat)
portfolioMeans = [2,5,6]
assert(computeSharpFromPortfolio(portfolio,means,returns) == computeSharp(portfolioMeans,cov, weights))


def linearSwap(portfolio, otherAsset,means, returns):
     for i in range(len(portfolio)):
         m, maxSharp  = portfolio[i], computeSharpFromPortfolio(portfolio,means,returns)
         old = portfolio[i]
         for j in otherAsset:
             portfolio[i] = j
             sharp = computeSharpFromPortfolio(portfolio,means,returns)
             if(sharp > maxSharp):
                 m = j
         portfolio[i] = m
         try:
             otherAsset.remove(m)
             otherAsset.append(old)
         except:
             pass       
     return portfolio

portfolio = [1,2]
otherAsset = [0,3,4]
returns= [[1,2,3],[1,2,3],[1,2,3],[1000,2000,3000],[500,800,900]]
means = [np.mean(i) for i in returns]
assert(linearSwap(portfolio,otherAsset,means, returns) == [4, 3])

portfolio = [1,2]
otherAsset = [0,3,4]
returns= [[1,2,3],[1,2,3],[1,2,3],[1,4,16],[1,2,3]]
means = [np.mean(i) for i in returns]
assert(linearSwap(portfolio,otherAsset,means, returns)[0] == 3)

portfolio = [0,1]
otherAsset = [2]
returns= [[1,2,3],[234,7,16],[-100,22,3]]
means = [np.mean(i) for i in returns]
sharp = [computeSharpFromPortfolio(i,means, returns) for i in [[1,2],[0,1],[0,2]]]
#print(sharp)
assert(linearSwap(portfolio,otherAsset,means, returns) == [2,1])

def _computePortfolio(listOfAllReturns,n):
    means = [np.mean(i) for i in listOfAllReturns]
    portfolio, otherAsset = getTheNBest(means,n)
    return linearSwap(portfolio, otherAsset, means, listOfAllReturns)

assert(_computePortfolio(returns,3) ==[1, 0, 2])
assert(_computePortfolio(returns,2) == [1,2])
def computePortfolio(listOfAllReturns):
    return _computePortfolio(listOfAllReturns,40)