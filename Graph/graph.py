#!/usr/bin/python
# -*- coding: UTF-8 -*-
#图的基本操作lalala可以是创建一个图也可以是读入一个图总之就是对一个图
#进行初始化，也可以从文件中读入
import Bag1
import Stack1
class Graph(object):
    #就是初始化用给定的顶点数目初始化
    def __init__(self,v):
        self.V = v
        self.E = 0
        self.adj = [None]*self.V
        for i in range(v):
            self.adj[i] = Bag1.Bag()#用来存储每一个顶点的相邻顶点
    def readinGraph(self,G):#用给定的现成的图进行初始化
        G = Graph()
        self.E = G.E()
        for v in range(G.V()):
            sta = Stack1()
            for i in G.adj(v):
                sta.push(i)
            for i in sta():
                self.adj[v].add(i)
    def V(self):
        return self.V
    def E(self):
        return self.E
    def addEdge(self,r,w):#连接两个顶点（对图进行修改）
        self.adj[r].add(w)
        self.adj[w].add(r)
        self.E += 1
    def degree(self,r):#与给定顶点相邻的顶点数目
        return self.adj[r].size()
#测试代码
g = Graph(2)
g.addEdge(0,1)
print g.degree(1)
