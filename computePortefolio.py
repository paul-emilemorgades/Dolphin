import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import quandl
import scipy.optimize as sco
import json
from sendPortfolio import createPortfolio, sendPortfolio, postsharpe
from req_get_actifs import changeCommaInPoint

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

def computeSharpFromPortfolio(portfolio, assets_id):
    json_porfolio = createPortfolio(portfolio,assets_id)
    usr = "EPITA_GROUPE2"
    pwd = "PcA7s3Rnzsch6M79"
    sendPortfolio(json_porfolio, usr, pwd)
    s = json.loads(postsharpe(usr,pwd).text)
    print(portfolio, "\n")
    a = float(changeCommaInPoint(s["1821"]["12"]["value"]))
    print(a, "\n" )
    return a
    
     


def linearSwap(portfolio, otherAsset,means, returns, assets_id):
     for i in range(len(portfolio)):
         m, maxSharp  = portfolio[i], computeSharpFromPortfolio(portfolio, assets_id)
         old = portfolio[i]
         for j in otherAsset:
             portfolio[i] = j
             sharp = computeSharpFromPortfolio(portfolio, assets_id)
             if(sharp > maxSharp):
                 m = j
         portfolio[i] = m
         try:
             otherAsset.remove(m)
             otherAsset.append(old)
         except:
             pass
     print(computeSharpFromPortfolio(portfolio,assets_id))
     return portfolio


def _computePortfolio(listOfAllReturns,n, assets_id):
    means = [np.mean(i) for i in listOfAllReturns]
    portfolio, otherAsset = getTheNBest(means,n)
    return linearSwap(portfolio, otherAsset, means, listOfAllReturns, assets_id)

def computePortfolio(listOfAllReturns, assets_id):
    return _computePortfolio(listOfAllReturns,40 , assets_id)