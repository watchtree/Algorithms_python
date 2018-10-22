#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/23 7:03
# software: PyCharm
# question: 跳台阶
'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
思路：类似于斐波拉契数列的变形
'''
class Solution:
    #v1.0运行时间：23ms占用内存：5720k
    #以列表形式保存中间数据
    def jumpFloor(self, number):
        temp = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                temp[(i+1)%2] = temp[0]+temp[1]
        return temp[(number+1)%2]

    #变态青蛙跳，跳n级台阶，一次最大跳n级的跳法为2^(n-1)
    def jumpFloor2(self, number):
        ans = 1
        if number >= 2:
            for i in range(number):
                ans = ans*2
        return ans

if __name__ == "__main__":
    test = Solution()

    print(test.jumpFloor2(5))