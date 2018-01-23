#!/usr/bin/python
# -*- coding: UTF-8 -*-
# prim的即时算法
import IndexMinPQ
import Queue1
class PrimMST(object):
    FLOATING_POINT_EPSILON = 1e-12
    def __init__(self,G):
        self.pq = IndexMinPQ(G.V())
        self.marked = [False]*G.V() # 判断顶点是不是在树上
        self.distTo = []  # 存放距离树最近的边的权重
        self.edgeTo = []  # 存放距离树最近的边
        for v in range(G.V()):
            self.distTo[v] = float("inf")
        for v in range(G.V()):
            if not self.marked[v]:
                self.prim(G,v)
    def prim(self,G,s):
        self.distTo[s] = 0.0
        self.pq.insert(s,self.distTo[s])
        while not self.pq.isEmpty():
            v = self.pq.delMin()
            self.scan(G,v)
    def scan(self,G,v):
        self.marked[v] = True
        for e in G.adj(v):
            w = e.other(v)
            if self.marked[w]:  # 直接在添加的时候就避免会产生无效边
                # 不会再优先队列中添加这么多的边所以比较省事
                continue
            if e.weight() < self.distTo[w]:  # 永远只保存最优的边每#
                # 次浏览都会更新最优化的边
                self.distTo[w] = e.weight()
                self.edgeTo[w] = e
                if self.pq.contains(w):
                    self.pq.decreaseKey(w,self.distTo[w])
                else:
                    self.pq.insert(w,self.distTo[w])
    def edges(self):
        mst= Queue1()
        for v in range(len(self.edgeTo)):
            e = self.edgeTo[v]
            if e != None:
                mst.enqueue(e)
        return mst
    def weight(self):
        weight = 0.0
        for e in self.edges():
            weight += e.weight()
        return weight