#!/usr/bin/python
# -*- coding: UTF-8 -*-
#撞击事件的描述，通过这个minpq的应用主要是掌握多个类联系在一起的面向对象的编程思想
import MinPQ
import Event
import Particle
class CollisionSystem(object):
    pq = MinPQ()
    t = 0.0
    particles = []
    def __init__(self,particles):#需要我们往里传的值就是一个微粒的对象
        self.particles = particles
        self.pq = MinPQ
        self.t = self.t
    def predict(self,a):
        a = Particle()
        if a == None:
            return
        for i in range(len(self.particles)):
            dt = a.timeToHit(self.particles[i])
            e = Event(self.t+dt,a,self.particles[i])
            self.pq.insert(e)
        e1 = Event(self.t+a.timeToHitVerticalWall(),a,None)
        e2 = Event(self.t+a.timeToHitHorizontalWall(),None,a)
        self.pq.insert(e1)
        self.pq.insert(e2)
    def simulate(self):
        for i in range(len(self.particles)):
            self.predict(self.particles[i])
            e3 = Event(0,None,None)
            self.pq.insert(e3)
        while not self.pq.isEmpty():
            event = self.pq.delMin()
            if not event.isValid():
                continue
            a = event.a
            b = event.b
            for i in range(len(self.particles())):
                self.particles[i].move(event.time - self.t)
            t = event.time
            if not a!=None and b != None:
                a.bounceOff(b)
            elif not a != None and b == None:
                a.bounceOffVerticalWall()
            elif not a == None and b != None:
                b.bounceOffHorizontalWall()
            elif a == None and b == None:
                pass
            self.predict(a)
            self.predict(b)