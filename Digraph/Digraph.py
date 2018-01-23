# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Bag1
import Stack1
class Digraph(object):
    def __init__(self, v):  # 自己构造一个自己定义顶点数量的有向图
        self.V = v
        self.E = 0
        self.indegree = [0]*v
        self.adj = [0]*self.V
        for i in range(self.V):
            self.adj[i] = Bag1.Bag()
    def V(self):
        return self.V
    def E(self):
        return self.E
    def addEdge(self,v,w):#v-->w
        self.adj[v].add(w) # adj[]就是从v可以到达的点,它的size就是外度
        self.indegree[w] += 1  # 内度加1
        self.E += 1
    def adj(self,v):
        return self.adj[v]
    def outdegree(self,v):
        return self.adj[v].size()
    def indegree(self,v):
        return self.indegree[v]
    def reverse(self):
        reverse = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                reverse.addEdge(w,v)
        return reverse

'''
    def __init__(self,filename):
        self.V = open(filename)[0]
        self.indegree = [0]*self.V
        self.adj = [0]*self.V
        for i in range(self.V):
            self.adj[i] = Bag1.Bag()
        self.E = open(filename)[1]
        for j in range(self.E):
            v =
            w =
            self.addEdge(v,w)
'''
     # 根据已经给定的图创建新的图
'''
    def __init__(self,g):
        self.E = g.E()
        for v in range(self.V):
            self.indegree[v] = g.indegree(v)
        for v in range(g.V()):
            reverse = Stack1.Stack()
            for w in g.adj[v]:
                reverse.push(w)'''