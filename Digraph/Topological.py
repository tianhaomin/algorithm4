# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 优先级限制下的调度问题其实就是计算有向无环图的所有顶点的拓扑顺序
# 只有有向无环图才能进行拓扑排序
import DirectedCycle
import DepthFirstOrder
class Toplogical(object):
    def __init__(self,g):
        self.G = g
        self.finder = DirectedCycle.DirectedCycle(self.G)
        if not self.finder.hasCycle():  #前提是没有环必须是DAG
            self.dfs = DepthFirstOrder.DepthFirstOrder(self.G)  # t拓扑顺序就是reversePOSTorder
            self.order = self.dfs.reversePost()
            self.rank = [0]*self.G.V
            i = 0
            for v in self.order:  #返回的是在拓扑顺序的序号
                self.rank[v] = i
                i += 1
    def order(self):
        return self.order
    def hasOrder(self):
        return self.order != None
    def rank(self,v):
        if self.hasOrder():
            return self.rank[v]
        else:
            return -1