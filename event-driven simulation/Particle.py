#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import math
class Particle(object):
    def __init__(self):
        self.rx = random.uniform(0.0,1.0)
        self.ry = random.uniform(0.0,1.0)
        self.vx = random.uniform(-0.005,0.005)
        self.vy = random.uniform(-0.005,0.005)
        self.mass = 0.5
        self.radius = 0.01
        self.count = 0
    def move(self,dt):
        if (self.rx + self.vx*dt)<self.radius or (self.rx + self.vx*dt)>1.0-self.radius:
            self.vx = -self.vx
        if (self.ry + self.vy*dt)<self.radius or (self.ry + self.vy*dt)>1.0-self.radius:
            self.vy = -self.vy
        self.rx = self.rx + self.vx*dt
        self.vy = self.ry + self.vy*dt
    def count(self):
        return self.count
    def timeToHit(self,that):
        if self == that:
            return float('inf')
        that = Particle()
        dx = that.rx - self.rx
        dy = that.ry - self.ry
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx+dy*dvy
        if dvdr>0:
            return float('inf')
        dvdv = dvx*dvx + dvy*dvy
        drdr = dx*dx + dy*dy
        sigma = that.radius - self.radius
        d = dvdr*dvdr-dvdr*(drdr-sigma*sigma)
        if d<0:
            return float('inf')
        return -(dvdr + math.sqrt(d))/dvdv
    def timeToHitVerticalWall(self):
        if self.vx>0:
            return (1.0-self.rx-self.radius)/self.vx
        elif self.vx<0:
            return (self.radius-self.rx)/self.vx
        else:
            return float('inf')
    def timeToHitHorizontalWall(self):
        if self.vy > 0:
            return (1.0 - self.ry - self.radius) / self.vy
        elif self.vy < 0:
            return (self.radius - self.ry) / self.vy
        else:
            return float('inf')
    def timeToHitHorizontalWall(self):
        if self.vy>0:
            return (1.0-self.ry-self.radius)/self.vy
        elif self.vy<0:
            return (self.radius - self.ry)/self.vy
        else:
            return float('inf')
    def bounceOff(self,that):
        that = Particle()
        dx = that.rx - self.rx
        dy = that.ry - self.ry
        dvx = that.vx - self.vx
        dvy = that.vy - self.vy
        dvdr = dx*dvx - dy*dvy
        dist = self.radius + that.radius
        magnitude = 2*self.mass*that.mass*dvdr/((self.mass+that.mass)*dist)
        fx = magnitude*dx/dist
        fy = magnitude*dy/dist
        self.vx += fx/self.mass
        self.vy += fy/self.mass
        self.vx -= fx/that.mass
        self.vy -= fy/that.mass
        self.count += 1
        that.count += 1
    def bounceverticalWall(self):
        self.vx = -self.vx
        self.count += 1
    def bounceoffHorizontalWall(self):
        self.vy = -self.vy
        self.count += 1

