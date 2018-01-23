#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
EPSILON = 1e-11
class FordFulkerson(object):
    def __init__(self,G,s,t):  # 流量网络。起点。终点
        self.value = self.excess(G,t)
        bottle = float("INFINITY")
        v = t
        while self.hasAugmentingPath(G,s,t):  #判断是不是存在可增加的边
            while not v == s:
                #  算出每一条边有多少流量可以用
                bottle = min(bottle, self.edgeTo[v].residualCapacityTo(v))
                v = self.edgeTo[v].other(v)
            v = t
            while not v == s :
                #  增加流量
                self.edgeTo[v].addResidualFlow(v,bottle)
            self.value += bottle

    def value(self):
        return self.value

    def inCut(self,v):
        return self.marked[v]

    def hasAugmentingPath(self,G,s,t):
        edgeTo = [0]*G.V()
        marked = [False]*G.V()
        queue = Queue1()
        queue.enqueue(s)
        marked[s] = True
        while not queue.isEmpty() and not marked[t]:
            v = queue.dequeue() #  检查队列中的每一个点可达的边
            #  是不是仍然存在剩余容量大于0的边也就是说仍有增益边
            for e in G.adj(v):
                w = e.other(v)
                if e.residualCapacityTo(w)>0:
                    if not marked[w]:
                        edgeTo[w] = e
                        marked[w] = True
                        queue.enqueue(w)
        return marked[t]

    def excess(self,G,v):  # 返回点v处的过流
        excess = 0.0
        for e in G.adj(v):
            if v == e.from1():
                excess -= e.flow()
            else:
                excess += e.flow()
        return excess  # 每个点处的进出流量应该是平衡的

    def isFeasible(self,G,s,t):  # 查看是不是满足容量限制
        for v in G.V():
            for e in G.adj(v):
                if (e.flow()<0.0 or e.flow()>e.capacity):
                    print "Edge does not satisfy capacity constraints:",e
                    return False
        #检查flow into a vertex equals zero除了原点与终点
        if abs(self.value + self.excess(G,s)) > 0.0:
            print