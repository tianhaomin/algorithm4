#!/usr/bin/python
# -*- coding: UTF-8 -*-
#流量边的构建
EPSILON = 1e-10
class FlowEdge(object):

    def __init__(self, v, w, capacity):
        # 从v->w的一条流量边
        self.v = v
        self.w = w
        self.capacity = capacity
        self.flow = 0.0
    '''
    def __init__(e)#用已知的流量边进行初始化
        self.v = e.v
        self.w = e.w
        self.capacity = e.capacity
        self.flow = e.flow
    '''
    def from1(self):
        return self.v

    def to1(self):
        return self.w

    def capacity(self):
        return self.capacity

    def flow(self):
        return self.flow

    def other(self,vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            return None
    # 剩余网络的构建基础
    def residualCapacityTo(self,vertex):
        if vertex == self.v:
            return self.flow  # 还剩多少可以减
        elif vertex == self.w:
            return self.capacity - self.flow  # 还剩多少可以加

    def addResidualFlowTo(self, vertex, delta):
        if vertex == self.v:
            self.flow -= delta  # 反向边
        elif vertex == self.w:
            self.flow += delta  # 正向边
        if abs(self.flow) <= EPSILON:
            self.flow = 0
        if abs(self.flow - self.capacity) <= EPSILON:
            self.flow = self.capacity