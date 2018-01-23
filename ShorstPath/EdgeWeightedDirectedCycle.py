#!/usr/bin/python
# -*- coding: UTF-8 -*-
#   在有向权重图中找到有向环
import Stack1


class EdgeWeightedDirectedCycle(object):


    def __init__(self,G):
        self.marked = [False]*G.V()
        self.onStack = [False]*G.V()
        self.edgeTo = [0]*G.V()
        self.cycle = Stack1()
        for v in range(G.V()):
            if not self.marked[v]:
                self.dfs(G,v)

    def dfs(self,G,v):  # 检查是拓扑顺序还是存在环路，基于深度优先搜素
        self.onStack[v] = True
        self.marked[v] = True
        for e in G.adj(v):
            w = e.to()
            if not self.cycle == None:
                return
            elif not self.marked[w]:
                self.edgeTo[w] = e
                self.dfs(G,w)
            elif self.onStack[w]:
                f = e
                while f.from1() != w:
                    self.cycle.push(f)
                    f = self.edgeTo[f.from1()]
                self.cycle.push(f)
                return
        self.onStack[v] = False

    def hasCycle(self):
        return self.cycle != None

    #判断是不是有环
    def cycle(self):
        return self.cycle
