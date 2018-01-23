#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re, collections
def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            if re.match(r'[a-zA-Z0-9]*', line):
                words_box.extend(line.strip().split())
    return collections.Counter(words_box)


print get_words('E:/er.txt')

#若想用BST实现词频统计需要正则匹配然后插入。关键问题是key（）
'''
minlen = 2
if word >=2:
    st.put(word,1)
if not st.contains(word):
    st.put(word,1)
else:
    st.put(word,st.get(word)+1)
    需要正则匹配
'''

