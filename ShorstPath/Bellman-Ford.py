#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
import EdgeWeightedDigraph
import EdgeWeightedDirectedCycle
import Stack1

class BellmanFordSP(object):


    def __init__(self,G,s):
        self.distTo = [0.0]*G.V()
        self.edgeTo = [0]*G.V()
        self.onQueue = [False]*G.V()
        for v in range(G.V()):
            self.distTo[v] = float("inf")
        self.distTo[0] = 0.0
        self.queue = Queue1()
        self.queue.enqueue(s)
        self.onQueue[s] = True
        self.cost = 0
        self.cycle = Stack1()
        while (not self.queue.isEmpty() and not self.hasNegativeCycle()):
            v = self.queue.dequeue()
            self.onQueue[v] = False
            self.relax(G,v)


    def relax(self,G,v):
        for e in G.adj(v):
            w = e.to()
            if self.distTo[w] > self.distTo[v] + e.weight():
                self.distTo[w] = self.distTo[v] + e.weight()
                self.edgeTo[w] = e
                if not self.onQueue[w]:
                    self.queue.enqueue(w)  # Bellman算法就是对边任意的进行放松总能得到最短路径
                    self.onQueue[w] = True
            if self.cost%G.V() == 0:
                self.cost += 1
                self.findNegativeCycle()
                if self.hasNegativeCycle():
                    return


    def hasNegativeCycle(self):
        return self.cycle


    def findNegativeCycle(self):
        V = len(self.edgeTo)
        spt = EdgeWeightedDigraph(V)
        for v in range(V):
            if self.edgeTo[v] != None:
                spt.addEdge(self.edgeTo[v])
        finder = EdgeWeightedDirectedCycle(spt)
        self.cycle = finder.cycle()

    def distTo(self,v):
        return self.distTo[v]

    def hasPathTo(self,v):
        return self.distTo[v]<float("INF")

    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = Stack1()
        e = self.edgeTo[v]
        while not e == None:
            path.push(e)
            e = self.edgeTo[e.from1()]
        return path

