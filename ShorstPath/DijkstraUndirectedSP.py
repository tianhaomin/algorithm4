#!/usr/bin/python
# -*- coding: UTF-8 -*-
#如何在无向图中找到最短路径
#思路就是在Dijkstra算法中把边都换成双向的就行
import IndexMinPQ
import Stack1
INF = float("inf")
class DijkstraUndirectedSP(object):
    def __init__(self,G,s):
        self.distTo = [0.0]*G.V()
        self.edgeTo = [0]*G.V()
        for v in range(G.V()):
            self.distTo[v] = INF
        self.distTo[s] = 0.0
        self.pq = IndexMinPQ(G.V())
        self.pq.insert(s,self.distTo[s])
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            for e in G.adj(v):
                self.relax(e,v)  # e是从顶点v发出的边
    def relax(self,e,v):
        w = e.other(v)  # e的另一个顶点
        if self.distTo[w] > self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e  # 存放最后一条到达w得边
            if self.pq.contains(w):
                self.pq.decreaseKey(w,self.distTo[w])
            else:
                self.pq.insert(w,self.distTo[w])
    def distTo(self,v):
        return self.distTo[v]
    def hasPathTo(self,v):
        return self.distTo[v] < INF
    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = Stack1()
        x = v
        e = self.edgeTo[v]
        while not e == None:
            path.push(e)
            x = e.other(x)
        return path