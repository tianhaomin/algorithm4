#!/usr/bin/python
# -*- coding: UTF-8 -*-
#集合的经典应用lalala
from SET import *
set = SET()
while not str == '-':
    str = raw_input('Please enter you words:')
    set.add(str)
str1 = raw_input('Please enter the key you want to find: ')
if set.contains(str1):
    print 'you find it'