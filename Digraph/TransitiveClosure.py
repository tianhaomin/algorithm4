# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 判断有向图中的顶点是不是可达的
import DirectedDFS
class TransitiveClosure(object):
    def __init__(self,g):
        self.G = g
        self.tc = [0]*self.G.V
        for v in range(self.G.V):
            self.tc[v] = DirectedDFS.DirectedDFS(self.G,v)
    def reachable(self,v,w):
        return self.tc[v].marked(w)  # 判断是不是可以从v到w
# DirectedDFS是给定一个顶点来已知进行深度优先搜索的，并不是
# 能对任意的点进行是不是联通的判断，而以上这段代码就是直接讨
# 论任意两个点是不不是可达的不必事先指定起始点