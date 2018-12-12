#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/22 7:32
# software: PyCharm
# question: 斐波拉契数列
'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(3)=2,F(n)=F(n-1)+F(n-2)（n>=4，n∈N*）
'''
'''
如何不使用递归实现斐波那契数列，需要把前面两个数字存入在一个数组中。
斐波那契数列的变形有很多，如青蛙跳台阶，一次跳一个或者两个；
铺瓷砖问题。变态青蛙跳，每次至少跳一个，至多跳n个，一共有f(n)=2n-1种跳法。考察数学建模的能力。
'''
class Solution:

    #v1.0 递归方法 时间的复杂度为O(2^n), 不通过在线，复杂度过大
    def Fibonacci(self, n):
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    #v2.0 非递归方法
    #利用数组进行每个数据的保存
    def Fibonacci2(self, n):
        if n <= 1:
            return n
        elif n == 2:
            return 1
        else:
            temp = []
            temp.append(1)
            temp.append(1)
            for i in range(2, n):
                temp.append(temp[i-1] + temp[i-2])
            return temp[n-1]

    #v3.0运行时间：23ms占用内存：5860k
    #占用内存少一些，将数组保留为两个位置，进行下一步计算，替换上一步的一个值
    def Fibonacci3(self, n):
        temp = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                temp[i%2] = temp[0] + temp[1]
        return temp[n%2]

if __name__ == "__main__":
    s = Solution()
    for i in range(29):
        print(s.Fibonacci3(i))