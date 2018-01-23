#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = ['4PGC938', '2IYE230', '3CIO720', '1ICK750', '1OHV845', '4JZY524', '1ICK750', '3CIO720', '1OHV845'
     , '1OHV845', '2RLA629', '2RLA629', '3ATW723']  # 待排数组
R = 256
aux = ['a'] * len(s)
w = int(raw_input("Please enter how many keys: "))  # 以多少个键作为排序的依据
d = w - 1
while d >= 0:
    count = {}
    for  i in range(len(s)):
        if not chr(ord(s[i][d])+1) in count:
            count[chr(ord(s[i][d]) + 1)] = 0
        else:
            count[chr(ord(s[i][d]) + 1)] += 1

    for r in range(R):
        count[chr(ord(r) + 1)] += count[chr(ord(r))]

    for i in range(len(s)):
        count[s[i][d]] += 1
        aux[count[s[i][d]]] = s[i]

    for i in range(len(s)):
        s[i] = aux[i]

    d -= 1

print s