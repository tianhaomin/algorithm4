#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import operator
#生成数据，训练集有监督学习lalala
def creatDataSet():
    dataset1 = [[1,3,5,'senior'],
                [1,2,1,'junior'],[1,3,2,'junior'],
                [2,1,5,'junior'],[2,3,6,'senior'],
                [2,2,5,'junior'],[2,5,6,'senior'],
                [3,4,5,'senior'],[3,3,4,'junior'],
                [4,6,3,'senior'],[4,2,1,'junior']]
    label = ['department','age','salary']
    Count  = 0.0
    count = [30,40,40,20,5,3,3,10,4,4,6]
    for i in count:
        Count += i
    dataset = []
    for i in dataset1:
        for j in count:
            for k in range(j):
                dataset.append(i)
    return dataset,label
#测试代码
# print creatDataSet() 成功

#算整个数据集的熵
#计算熵，计算给定数据集的熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * math.log(prob,2) #log base 2
    return shannonEnt
#测试函数lalaal
'''a,b,c,d = creatDataSet()
print calcShannonEnt(a)
'''
#将符合的要用来分类的属性从符合的个体中删除
#这一步存在的意义是在于为了以后计算信息增量，算某一特征的信息增益其实就是算出去他意外子集的信息增益效果是一样的
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for l in dataSet:
        if l[axis] == value:
            reducedItem = l[:axis]  # chop out axis used for splitting
            reducedItem.extend(l[axis + 1:])#把符合的属性去除
            retDataSet.append(reducedItem)
    return retDataSet#拆分这一部分的函数是将符合我们需求的数据拿出来统计数量
#选择增益最大的属性进行分类
#选择最好的子集的方法就是先将一部分作为dataset，看看其中包含多少个可以分割的属性
#对美一个分割求其信息量在进行比较
def chooseBestFeatureToSplit(dataSet):
    lenItem = len(dataSet[0]) - 1#数据集中的珂用于分裂的特征个数
    bestatrr = -1
    baseInfo = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    for i in range(lenItem):  # iterate over all the features
        featList = [example[i] for example in dataSet]  # create a list of all the examples of this feature
        uniqueVals = set(featList)  # 得到了一个特征的所有分裂方式
        newInfo = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newInfo += prob * calcShannonEnt(subDataSet)
        infoGain = baseInfo - newInfo  # calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):  # compare this to the best gain so far
            bestInfoGain = infoGain  # if better than current best, set to best
            bestatrr = i
    return bestatrr  # ret
#测试代码lalala
'''
a,b,c,d = creatDataSet()
print a
print calcShannonEnt(a)
print chooseBestFeatureToSplit(a)'''
#表决就是当所有属性都处理完依旧没有将一些数据分好类就需要白哦绝其类别
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
#创建树的代码，对数据集和label的格式都得更改尤其label的格式得更改
#前面没设计label此时需要label配合得到可读的树结构使结果可读
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]#得到dataset的所有标签
    if classList.count(classList[0]) == len(classList):#如果只有数据集中只有一个标签那么就停止
        return classList[0]  # stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:  # 数据集中的数据只有一个标签项
        return majorityCnt(classList)#返回表决结果
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]  # 将副本传递给新的列表防止改变新的列表时将原来的也改变了。
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
#测试代码
data,label = creatDataSet()
print createTree(data,label)









