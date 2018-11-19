#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/19 7:44
# software: PyCharm
#question: 和为S的两个数字
'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的
'''
'''
：设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，
如果和大于目标值，则把后一个指针前移，如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到，就终止操作。
'''
class Solution:

    #运行时间：28ms用内存：8668k
    def FindNumbersWithSum(self, array, tsum):
        length = len(array)
        if length < 3:
            return []
        small = 0
        big = length-1
        numsProduct = (tsum//2+1)**2
        while small < big:
            curNum = array[small] + array[big]
            if curNum == tsum:
                if array[small]*array[big] < numsProduct:
                    result = [array[small], array[big]]
                    numsProduct=array[small]*array[big]
                small += 1
            if curNum < tsum:
                small += 1
            if curNum > tsum:
                big -= 1
        if numsProduct == (tsum//2+1)**2:
            return []
        else:
            return result
    #因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小 # 所以直接输出查找到的第一对数即可
    # 运行时间：27ms占用内存：5724k
    def FindNumbersWithSum2(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array) - 1
        while start < end:
            sum = array[start] + array[end]

            if sum < tsum:
                start += 1
            elif sum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]

        return []

    def FindNumberWithSum3(self, array, tsum):
        ls = []
        if not isinstance(array, list):
            return ls #判定数组是否为list类型
        for i, v in enumerate(array):#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for v1 in array[i:]:#遍历数组的第i个之后的数字
                if (v+v1) == tsum:
                    ls.append([v, v1])
        if ls:
            return ls[0]
        else:
            return ls



test = [1,2,4,7,11,16]
s = Solution()
print(s.FindNumbersWithSum2(test, 10))


