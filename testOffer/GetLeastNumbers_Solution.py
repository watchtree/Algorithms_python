#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/9 11:47
# software: PyCharm
# question: 最小的K个数字
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,
'''
'''
两种方法。
第一种方法是基于划分的方法，如果是查找第k个数字，第一次划分之后，划分的位置如果大于k，
那么就在前面的子数组中进行继续划分，反之则在后面的子数组继续划分，时间复杂度O(n)；
第二种方法是可以适用于海量数据的方法，该方法基于二叉树或者堆来实现，
首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，
如果遍历到的元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，
最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。
'''
class Solution:
    #辅助函数，快排所用的Partition划分
    def Partition(self, numbers, length, start, end):
        if numbers == None or length<=0 or start<0 or end>=length:
            return None
        if end == start:
            return end
        piotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end
        done = False
        while not done:
            while numbers[leftmark]<=piotvlue and leftmark<=rightmark:
                leftmark += 1
            while numbers[rightmark]>=piotvlue and rightmark>=leftmark:
                rightmark -= 1
            if leftmark > rightmark:
                done = True
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark
    #基于划分的方法O（n）
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput)<=0 or k<=0:
            return []
        n = len(tinput)
        start = 0
        end = n - 1
        #进行初始划分判定，获得index
        index = self.Partition(tinput, n, start, end)
        while index != k-1:#如index=k-1则说明，k-1之前经过排序都小于同一个数字前k个
            if index>k-1:
                #若index大于k-1，在前面的数字中继续进行划分，知道index=k-1
                end = index-1
                index = self.Partition(tinput, n, start, end)
            else:
                #反之在后面的数字进行划分
                start = index + 1
                index = self.Partition(tinput, n, start, end)
        output = tinput[:k]#对前k个数字进行排序，获得最小四个数字
        output.sort()
        return output

    ## O(nlogk)的算法, 适合海量数(线上测试未通过)
    # 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
    def GetLeastNumbers(self, tinput, k):
        import heapq
        #heapq 模块提供了堆算法。heapq是一种子节点和父节点排序的树形数据结构
        if tinput == None or len(tinput)<k or len(tinput) <= 0 or k<=0:
            return []
        output = []
        for number in tinput:
            if len(output)<k:
                output.append(number)#将前k个数据固定在前k个
            else:
                #构造最大堆
                output = heapq.nlargest(k, output)#函数作用是堆排序，在由后向前取k个
                #heapq模块实现了一个适用于Python列表的最小堆排序算法。
                #去一个列表中数值最大的3个元素。
                if number>=output[0]:
                    continue
                else:
                    output[0] = number
        return  output[::-1]
tinput = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers(tinput, 4))
print(s.GetLeastNumbers(tinput, 5))