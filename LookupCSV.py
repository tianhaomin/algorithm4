#!/usr/bin/python
# -*- coding: UTF-8 -*-
#在一个文件中指定键和值的位置进行查询lalala
f = open('E:/3G.txt.txt')
s = f.readlines()
key = []
#在文件中指定键值各自对应的部分
for i in range(len(s)):
    s[i] = s[i].split(' ')
for i in range(len(s)):
    key.append(s[i][0])
#需要剔除重复的键
temp1 = set(key)
keyList = list(temp1)
csv = {}#一个键可以对应多个值
for i in keyList:
    csv[i] = []
for i in s:
    if i[0] in keyList:
        csv[i[0]].append(i[1])
N = raw_input('Please enter which partern: ')
while N == 'Y':
    x = raw_input("Please enter what you want to find : ")
    if x in keyList:
        print csv[x]
    else:
        print 'sorry'
#实现反向索引,将所有对应的value全都返回
while N == 'N':
    x = raw_input("Please enter your value")
    k = []
    for i in csv:
        if x in csv[i]:
            k.append(i)
    print k

