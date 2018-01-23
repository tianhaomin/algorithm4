#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 寻找最长路径
import Stack1
from Digraph import Topological
class AcyclicLP(object):


    def __init__(self,G,s):

        self.distTo = [0.0]*G.V()
        self.edgeTo = [0] * G.V()
        for v in range(G.V()):
            self.distTo[v] = float("-inf")
        self.distTo[s] = 0.0
        #引入拓扑排序按照拓扑的顺序进行处理
        topological = Topological(G)
        for v in topological.order():
            for e in G.adj(v):
                self.relax(e)


    def relax(self,e):

        v = e.from1()
        w = e.to1()
        if self.distTo[w] < self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e

    def distTo(self,v):

        return self.distTo[v]


    def hasPathTo(self,v):

        return self.distTo[v] > float("-inf")


    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path  = Stack1()
        e = self.edgeTo[v]
        while not e == None:
            path.push(e)
            e = self.edgeTo[e.from1()]
        return path