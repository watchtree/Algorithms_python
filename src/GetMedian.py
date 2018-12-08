#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/8 8:48
# software: PyCharm
# question: 数据流中的中位数
'''
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数
'''
'''
构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。
当目两堆总数为偶数的时候，把数字存入最大堆，
当前两堆总数为奇数的时候，把数字存入最小堆
步骤：
重排最大堆，如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，
重排最小堆，如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换
重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数。
'''

#运行时间：29ms占用内存：5744k
class Solution:
    #输入直接利用原有sort排序的方法
    def __init__(self):
        self.data = []
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()
    def GetMedian(self, data):
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length//2] + self.data[length//2-1])/2.0
        else:
            return self.data[int(length//2)]

class Solution2:
    #运行时间：33ms占用内存：5732k
    def __init__(self):
        #左右堆分别为最大堆和最小堆
        #目前两堆总数为偶数的时候，把数字存入最大堆
        self.left = []
        self.right = []
        self.count = 0
    def Insert(self, num):
        #输入数据放入两个堆，奇数个数存一个， 偶数个数存一个
        if self.count & 1 == 0:
            #n和1做“按位与”运算
            #偶数成立，当总数为偶数时，存入最大堆
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1
    def GetMedian(self, x):
        #如果只有一个数字，直接返回
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length//2-1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2*k < length-1:
                index = 2*k+1
                if index < length - 1:
                    if alist[index] < alist[index+1]:
                        index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

