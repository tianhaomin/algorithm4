#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue1
import Wq#做是否联通的判断
import MinPQ#最小优先队列
class KruskalMST(object):
    def __init__(self,G):
        self.weight = 0.0  # 最小生成树的总权重
        self.mst = Queue1()
        self.pq = MinPQ()#将所有边按权值从小到达的顺序排列
#为什么不用序列，因为权值的大小是边这一对象上的附带品
        for e in G.edges():
            self.pq.insert(e)
        self.uf = Wq()#用一个连通域判断是不是会形成环
        #运行贪心算需要遍历最小优先队列中的所有边
        while (not self.pq.isEmpty() and self.mst.size()<G.V()-1):
            e = self.pq.delMin()
            v = e.either()
            w = e.other(v)#找到这天边的两个端点
            if not self.uf.connected(v,w):#判断v,w是不是在一个联通域内
                self.uf.union(v,w)
                self.mst.enqueue(e)
                self.weight += e.weight
    def edges(self):
        return self.mst
    def weight(self):
        return self.weight
