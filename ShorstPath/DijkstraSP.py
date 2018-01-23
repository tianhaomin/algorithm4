#!/usr/bin/python
# -*- coding: UTF-8 -*-
import IndexMinPQ
import Stack1
INF = float("inf")


class DijkstraSP(object):
    def __init__(self,G,s):
        self.distTo = [0.0]*G.V()
        self.edgeTo = [0]*G.V()
        for v in range(G.v):
            self.distTo[v] = INF
        self.distTo[s] = 0.0
        self.pq = IndexMinPQ(G.V())
        self.pq.insert(s,self.distTo[s])
        while not self.pq.isEmpty():  # 因为每个点都需要松弛
            v = self.pq.delMin()  # 我们每次都是松弛权重最小的
            #  1点所以用优先队列来退出最小权重的点
            for e in G.adj(v):
                self.relax(e)  # 松弛指定的边

    def relax(self, e):  # 松弛边
        v = e.from1()  # e的起点
        w = e.to1()  # e的终点
        if self.distTo[w] > (self.disTo[v] + e.weight()):  # 如果说发现原本的最短距离大那么就更新他的最短距离
            self.distTo[w] = self.distTo[v] + e.weight()
            self.edgeTo[w] = e
            if self.pq.contains(w):  # 往优先队列中添加值
                self.pq.decreaseKey(w,self.distTo[w])
            else:
                self.pq.insert(w,self.distTo[w])

    def distTo(self, v):
        return self.distTo[v]

    def hasPathTo(self, v):
        return self.distTo[v] < INF

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack1()  # 堆栈后进先出LIFO
        e = self.edgeTo[v]
        while not e == None:
            path.push(e)
            e = self.edgeTo[e.from1()]  # 一个个从指定顶点追回整个路径
        return path
