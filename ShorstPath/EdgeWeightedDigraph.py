#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Bag1
class EdgeWeightedDigraph(object):
    def __init__(self,V):
        #用边的数量和0条边初始化
        self.V = V
        self.E = 0
        self.indegree = [0]*self.V
        adj = [0]*self.V
        for v in range(self.V):
            adj[v] = Bag1()
    '''
    from numpy import random as nr
    可以用边与顶点一起初始化
    def __init__(self,V,E):
        self.V = V
        self.E = E
        for i in range(self.E):
            v = nr.uniform(self.V)
            w = nr.uniform(self.V)
            weight = 0.01*nr.uniform(100)
            e = DirectedEdge(v,w,weight)
            self.addEdge(e)
    '''
    '''
    可以从输入初始化函数
    def __init__(self):
        self.E = input()
        for i in range(self.E):
        v = input
        w = input
        weight = input
        self.addEdge(DirectedEdge(v,w,weight))
    '''
    '''
    #可以用一个图来更新
    import Stack1
    def __init__(self.G):
        self.E = G.E()
        for v in range(G.V()):
            self.indgree[v] = G.indegree(v)
        for v in range(G.V()):
            reverse = Stack1()
            for e in G.adj[v]:
                reverse.push(e)
            for e in reverse:
                adj[v].add(e)
    '''
    def V(self):
        return self.V
    def E(self):
        return self.E
    def addEdge(self,e):
        v = e.from1()
        w = e.to()
        self.adj[v].add(e)
        self.indegree[w] += 1
        self.E += 1
    def adj(self,v):
        return self.adj[v]
    def outdegree(self,v):
        return self.adj[v].size()
    def indegree(self,v):
        return self.indegree[v]
    def edges(self):
        list = []
        for v in range(self.V):
            for e in self.adj(v):
                list.append(e)
        return list
