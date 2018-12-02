#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/3 7:31
# software: PyCharm
# question: 字符流中第一个不重复的字符
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''
class Solution:
    # 运行时间：25 ms占用内存：5728k
    #字符流存储
    def __init__(self):
        self.adict = {}
        self.alist = []
    # 返回对应char'
    #引入两个辅助存储空间。
    # 一个Dict存储当前出现的字符以及字符出现的次数，一个List存储当前出现字符。
    # 然后每次比较List的第一个字符在Dict中对应的次数，如果为1则输出这个字符，如果不为1则弹出这个字符比较下一个字符。
    def FirstAppearingOnce(self):
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return "#"
        else:
            return self.alist[0]

    #输入字符
    def Insert(self, char):
        if char not in self.adict:
            self.adict[char] = 1
            self.alist.append(char)
        elif self.adict[char]:
            self.adict[char] = 2
