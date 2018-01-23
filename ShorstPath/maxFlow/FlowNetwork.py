#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 为解决最大流问题构建的流量网络，以之前的流量边为基础
import Bag1

class FlowNetwork(object):

    def __init__(self, V):
         # 给定顶点的数量进行初始化
        self.V = V
        self.E = 0
        self.adj = Bag1[V]
        for v in range(V):
            self.adj[v] = Bag1()
    '''
    给顶点数量和给定边数量进行初始化
    def __init__(self,E,V):
        for i in range(E):
            v =
            w =
            capacity =
            flowEdge = FlowEdge(v,w,capacity)
            self.addEdge(flowEdge)

    还可以直接从输入端直接输入初始化
    '''

    def V(self):
        return self.V

    def E(self):
        return self.E

    def addEdge(self,e):
        v = e.from1()
        w = e.to1()
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def adj(self,v):
        return self.adj[v]

    def edges(self):
        list = Bag1()
        for v in range(self.V):
            for e in self.adj[v]:
                if e.to1() != v:
                    list.add(e)
        return list