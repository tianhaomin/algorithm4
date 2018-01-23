#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Particle
class Event(object):
    a = Particle()
    b = Particle()
    time = 0.0
    countA = 0
    countB = 0
    def __init__(self,t,a,b):
        self.a = a
        self.b = b
        self.time = t
        if not a == None:
            self.countA = self.a.count()
        else:
            self.countA = -1
        if not b == None:
            self.countB = self.b.count()
        else:
            self.countB = -1
    def compareTo(self,that):
        that = Event()
        return self.time - that.time
    def isValid(self):
        if (self.a != None) and (self.a.count() != self.countA):
            return False
        if (self.b != None) and (self.b.count() != self.countB):
            return False
        return True

#主函数测试代码
