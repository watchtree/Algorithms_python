#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/29 9:06
# software: PyCharm
# question: 把字符串转换成整数
'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。
'''
'''
主要是区分输入和合法性，比如输入一个None，输入一个空字符串 ""，或者输入的字符串中含有“+”或者“-”，或者输入的字符串中含有除去+ — 数字的非数字字符，如何段应正常的输出还是报错，需要考虑的全面一些。
'''
class Solution:
    # 运行时间：32ms占用内存：5752k
    def StrToInt(self, s):
        flag = False
        if s == None or len(s) < 1:
            return 0
        numStack = []
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in dict:
                numStack.append(dict[i])
            elif i == "+":
                continue
            elif i == "-":
                continue
            else:
                return 0
        ans = 0
        if len(numStack) == 1 and numStack[0] == 0:
            flag = True
            return 0
        for i in numStack:
            ans = ans*10+i
        if s[0] == "-":
            ans = - ans
        return ans

S = Solution()
print(S.StrToInt("123"))