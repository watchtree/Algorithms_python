#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/28 8:38
# software: PyCharm
# question: 求1+2+3+。。+n
'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
class Solution:
    '''
    利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。
    如果对n连续进行两次反运算，那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。
    '''
    #运行时间：28ms占用内存：5752k
    def Sum_Solution(self, n):
        return self.sumN(n)
    def sum0(self, n):
        return 0
    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}#字典形式做一个条件判断
        return n+fun[not not n](n-1) # 利用非0值作两次非运算返回false, 0作两次非运算返回True

    #递归方法运行时间：27ms占用内存：5752k
    def Sum_Solution2(self, n):
        return n and self.Sum_Solution2(n-1) + n

s = Solution()
print(s.Sum_Solution2(5))