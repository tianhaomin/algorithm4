#!/usr/bin/python
# -*- coding: UTF-8 -*-
#词频统计，从文件读取内容正则匹配好好参考
import collections
def get_words(file):
    with open(file) as f:
        words_box = []
        for line in f:
            words_box.extend(line.lower().strip().split())
        new_words_box = []
        for word in words_box:
            if word.isalpha():
                new_words_box.append(word)
            else:
                new_word = ''
                for letter in word:
                    if letter.isalpha():
                        new_word += letter
                if new_word != '':
                    new_words_box.append(new_word)
    return collections.Counter(new_words_box)


print(get_words('emma.txt') + get_words('伊索寓言.txt'))