# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:11:00 2020

@author: Pio
"""
import numpy as np
import scipy.stats 

def computeAveragePearsonr(index, allAssets):
    moy = 0
    for i in range(len(allAssets)):
        if(i != index):
            moy += abs(scipy.stats.pearsonr(allAssets[index], allAssets[i])[0])
    return moy/(len(allAssets) -1)

tab = range(10)
tab2 = [i *-1 for  i in range(10)]
assert(computeAveragePearsonr(0, [tab, tab, tab]) == 1)
assert(computeAveragePearsonr(0, [tab, tab, tab2]) == 1)

def sortByAveragePearsonr(allAssets):
    dic = {}
    for i in range(len(allAssets)):
        dic[i] = computeAveragePearsonr(i, allAssets)
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
    return dic


assert(str(sortByAveragePearsonr([tab, tab, tab2])) == """{0: 1.0, 1: 1.0, 2: 1.0}""")
tab3 = [34,12,1,7,8888,9,0, 55,78,-34]

assert(str(sortByAveragePearsonr([tab, tab3, tab2])) == """{1: 0.05743356147616795, 0: 0.5287167807380839, 2: 0.5287167807380839}""")

def bestPearsonr(allAssets):
    dic = sortByAveragePearsonr(allAssets)
    tab = [i for i in dic.items()]
    tab = tab[:len(tab)//2]
    return {k:v for k,v in tab}

assert(str(bestPearsonr([tab, tab3, tab2, tab])) == """{1: 0.05743356147616795, 0: 0.6858111871587226}""")
    