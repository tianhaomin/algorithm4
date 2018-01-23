# !/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
import Stack1
class BreadthFirstDirectedPaths(object):
    def __init__(self,g,s): # 单个顶点，也可以由多个顶点的
        self.G = g
        self.S = s
        self.marked = [False]*self.G.V
        self.distTo = [0]*self.G.V
        self.edgeTo = [0]*self.G.V
        self.bfs(s)
    def bfs(self,s): # 现将原点放到队列中然后进行对她相邻带你的寻找
        #再一一对相邻点进行排查标记路径也进行时最短的路径
        q = Queue1.Queue()
        self.marked[s] = True
        self.distTo[s] = 0
        q.enqueue(s)
        while not q.isEmpty():
            v = q.dequeue()
            for w in self.G.adj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] +1
                    self.marked[w] = True
                    q.enqueue(w)
    def hasPathTo(self,v):
        return self.marked[v]
    def distTo(self,v):
        return self.distTo[v]
    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = Stack1.Stack()
        x = v
        while not self.distTo[x] == 0:
            path.push(x)
            x = self.edgeTo[x]
        path.push(x)
        return path