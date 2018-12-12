#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/29 8:38
# software: PyCharm
# question: 不用加减乘除做加法
'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
'''
将两个数的加法看作两步，
第一步是两个数相加但是不进位，
第二步是记录之前的两数相加应该进位的地方加上前一个相加但是不进位的数。(在二进制条件下直接用异或^计算)
对于具体的两个不小于0的数m和n，
第一步可以看做m和n的异或运算m^n，
第二步可以看做m和n的与运算然后左移一位得到实际的进位位置(m&n)<<1。（与运算，若TRue需要进位）
然后把两个得到的数字加起来继续操作，指到carry进位为0终止操作
'''
class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum  #异或运算结果
            num2 = carry #进位结果
            #将现加结果与进位结果相加继续进行进位运算知道无进位
        return num1

    #补码、反码、问题导致负数与正数相加无限循环
    def Add2(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF #每次对num1进行与操作保证是一个32位的整形
        return num1 if num1 >> 31 == 0 else num1 - 4294967296 #判断符号位是否为1做处理
s = Solution()
print(s.Add(-5, 2))