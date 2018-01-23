#!/usr/bin/python
# -*- coding: UTF-8 -*-
#在无环有向图的情况下来进行最短路径的搜索
from Digraph import Topological
import Stack1
INF = float("INF")
class AcylicSP(object):
    def __init__(self,G,s):
        self.distTo = [0.0]*G.V()
        self.edgeTo = [0]*G.V()
        for v in range(G.V()):
            self.distTo[v] = INF
        self.distTo[s] = 0.0
        self.topological = Topological(G)
        for v in self.topological.order():
            for e in G.adj(v):
                self.relax(e)

    def relax(self,e):
        v = e.from1()
        w = e.to1()
        if self.distTo[w] > self.distTo[v] + e.weight():
            self.distTo[v] = self.distTo[v] + e.weight()
            self.edge[w] = e

    def distTo(self,v):
        return self.distTo[v]

    def hasPathTo(self,v):
        return self.distTo[v] < INF
    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = Stack1()
        e = self.edgeTo[v]
        while not e == None:
            path.push(e)
            e = self.edgeTo[e.from1()]
        return path


