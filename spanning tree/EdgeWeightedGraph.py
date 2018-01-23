#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 根据权重的边来构建权重图
import Bag1
import Edge
import random
class EdgeWeightedGraph(object):

    #用v个顶点和0条边初始化
    def __init__(self,V):
        self.V = V
        self.E = 0
        self.adj = Bag1()
        for v in range(V):
            self.adj[v] = Bag1()
    '''
    #用给定的图初始化
    def __init__(EdgeWeightedGraph G):
    #从输入端初始化
    def __init__(In in):

    #用V个顶点和E条边初始化
    def __init__(self,V,E):
        self.V = V
        self.E = E
        self.adj = [0]*self.V
        for i in range(E):
            v = random.uniform(0,V)
            w = random.uniform(0,V)
            weight = random.uniform(0,1)
            e = Edge(v,w,weight)
            self.addEdge(e)
            '''
    def V(self): # 返回顶点的个数
        return self.V
    def E(self): # 返回边的个数
        return self.E
    def addEdge(self,e):
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1  # 如果用0条边初始化就需要这么做
    def adj(self,v): # 返回与顶点v相连的边
        return self.adj[v]
    def degree(self,v):
        return self.adj[v].size()
    # 返回图中所有的边
    def edges(self):
        list = Bag1()
        for v in self.V:
            selfLoops = 0
            for e in self.adj(v): # 与v相邻的边每一个e的端点都有一个是v
                if e.other(v)>v:
                    list.add(e)
                elif e.other(v)==v: #没有e,other(v)<v的情况为了避免重复
                    if selfLoops%2==0:
                        list.add(e)
                    selfLoops += 1
        return list
    def toString(self):
        pass