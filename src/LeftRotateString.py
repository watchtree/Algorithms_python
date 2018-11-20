#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/20 13:19
# software: PyCharm
# question： 左旋转字符串
'''
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
class Solution:
    #运行时间：32ms占用内存：5624k
    def LeftRotateString(self, s, n):
        if s == "":
            return ""
        if n == 0:
            return s
        m = len(s)
        n = n % m
        sList = list(s)
        for i in range(n):
            temp = sList.pop(0)
            sList.append(temp)
        return "".join(sList)
    '''
    首先需要写一个reverse函数，把任何输入的字符串完全翻转。
    然后根据题目中给出的左
    旋转字符串的个数n，用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分别旋转前[:length - n]子串和[length - n:]
    子串，重新拼接两个子串即可。
    '''
    # 运行时间：30ms占用内存：5708k
    #使用内置反转函数
    def LeftRotateString2(self, s, n):
        if s == "":
            return ""
        if n == 0:
            return s
        m = len(s)
        n = n % m
        sList = list(s)
        sList1 = sList[:n]
        sList1.reverse()
        sList2 = sList[n:]
        sList2.reverse()
        sList = sList1+sList2
        sList.reverse()
        return "".join(sList)

    #自编写反转函数
    def Reverse(self, alist):

s= "abcXYZdef"
n = 3
S = Solution()
print(S.LeftRotateString2(s, n))