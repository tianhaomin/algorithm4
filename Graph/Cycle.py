#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Stack1
class Cycle(object):
    def __init__(self,g):
        self.G = g
        self.marked = [False]*self.G.V()
        self.edgeTo = [0]*self.G.V()
        self.cycle = Stack1.Stack()
        for v in range(self.G.V()):
            if not self.marked[v]:
                self.dfs(self.G,-1,v)

    def hasSelfLoop(self):
        for v in range(self.G.V()):
            for w in self.G.adj():
                if v == w:
                    self.cycle = Stack1.Stack()
                    self.cycle.push(v)
                    self.cycle.push(v)
                    return True
        return False

    def hasParalleEdges(self):
        self.marked = [False]*self.G.V()
        for v in range(self.G.V()):
            for w in self.G.adj(v):
                if self.marked[w]:
                    self.cycle = Stack1.Stack()
                    self.cycle.push(v)
                    self.cycle.push(w)
                    self.cycle.push(v)
                self.marked[w] = True
            for w in self.G.adj[v]:
                self.marked[w] = False
        return False

    def hasCycle(self):
        return self.cycle != None

    def dfs(self,u,v):
        self.marked[v] = True#v代表的是顶点的标号
        for w in self.G.adj[v]:
            if self.cycle != None:
                return
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(self.G,v,w)
            if not w == u:
                self.cycle = Stack1.Stack()
                x = v
                while not x == w:
                    self.cycle.push(x)
                    x = self.edgeTo[x]
                self.cycle.push(w)
                self.cycle.push(v)