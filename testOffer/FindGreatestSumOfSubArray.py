#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/10 20:11
# software: PyCharm
# question: 连续子数组的最大和
'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
'''
关键的问题在于成功分析整个过程
对于连续子数组，可以用一个数值来存储当前和，
如果当前和小于零，那么在进行到下一个元素的时候，直接把当前和赋值为下一个元素，
如果当前和大于零，则累加下一个元素，同时用一个maxNum存储最大值并随时更新。也可以利用动态规划解决。
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None:
            return 0
        nCurSum = 0 #用于存储当前和，其会保存基本除了结点之外所有大于0的数字
        nGreatestSum = array[0]#用于保存的最大值
        for i in range(len(array)):
            if nCurSum <= 0:
                #如果当前和小于0， 则就算后续有数字可以补上，也不如本身数值大
                nCurSum = array[i]#所以在这个数值重新开始新的序列数值
            else:
                nCurSum = nCurSum+array[i]#如果当前值小于当前和，则直接相加
            if nCurSum > nGreatestSum:
                #如果有进步，对整个序列最优值进行更新
                nGreatestSum = nCurSum
        return nGreatestSum

    #动态规划的方法
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array)<=0:
            return 0
        alist = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or alist[i-1] <= 0:
                alist[i] = array[i]
            else:
                alist[i] = alist[i-1]+array[i]
        return max(alist)


array = [6, -3, -2, 7, -15, 1, 2, 2]
S = Solution()
print(S.FindGreatestSumOfSubArray2(array))