#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/24 8:17
# software: PyCharm
# question: 矩形覆盖
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
#同样类似于斐波拉契数列
class Solution:
    #解析见Fibonacci.py和jumpFloor.py
    def rectCover(self, number):
        if number<=2:
            return number
        temp = [1, 2]
        for i in range(3, number+1):
            temp[(i+1)%2] = temp[0] + temp[1]
        return temp[(number+1)%2]
