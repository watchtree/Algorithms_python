#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/2 14:33
# software: PyCharm
# question: 表示数值的字符串
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

class Solution:
    # s字符串转化为list 以E分割两边判定运行时间：26ms# 占用内存：5752k
    def isNumeric(self, s):
        if s == None or len(s) <= 0:
            return False
        s = s.lower()
        aList = [w for w in s]
        if 'e' in aList:
            indexE = aList.index('e')
            if indexE == 0 or indexE == len(s)-1:
                return False
            front = aList[:indexE]
            behind = aList[indexE+1:]
            if '.' in behind or len(behind) == 0:
                return False
            isFront = self.scanDight(front)
            isBehind = self.scanDight(behind)
            return isBehind and isFront
        else:
            return self.scanDight(aList)

    def scanDight(self, alist):
        dotNum = 0
        allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(alist)):
            if alist[i] not in allowVal:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:
                return False
            if dotNum > 1:
                return False
        return True


s = Solution()
print(s.isNumeric("12E"))