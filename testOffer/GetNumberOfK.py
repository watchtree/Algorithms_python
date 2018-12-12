#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/16 7:56
# software: PyCharm
# question: 数字再排序数组中出现的次数
'''
统计一个数字在排序数组中出现的次数。
'''
class Solution:

    #运行时间：32ms占用内存：5732k
    #二分查找
    def GetNumberOfK(self, data, k):
        if len(data)==0:
            return 0
        length = len(data)
        if length == 1 and data[0]==k:
            return 1
        if length == 1:
            return 0
        start = 0
        end = length-1
        midIndex = (end - start)//2+start
        while(data[midIndex]!=k):
            if data[midIndex]<k:
                start = midIndex+1
            else:
                end = midIndex-1
            if start > end:
                return 0
            midIndex = (end-start)//2+start
        leftCount = 0
        rightCount = 0
        leftIndex = midIndex-1
        rightIndex = midIndex+1
        while(leftIndex>=0 and data[leftIndex]==k):
            leftCount += 1
            leftIndex -= 1
        while(rightIndex<length and data[rightIndex]==k):
            rightCount += 1
            rightIndex += 1
        return 1+leftCount+rightCount

    #运行时间：32ms占用内存：5628k
    def GetNumberOfk(self, data, k):
        count = len(data)
        i = 0
        for j in range(count):
            if data[j] == k:
                i += 1
        return i