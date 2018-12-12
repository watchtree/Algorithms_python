#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/9 9:02
# software: PyCharm
# question: 滑动窗口的最大值
'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
 {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}
'''

'''
我们把可能成为滑动窗口的最大值的数值下标存入一个两端开口的队列index中。
首先遍历输入数组，在遍历次数小于窗口长度的时候，
如果index数组里面含有元素而且元素后面的下标值对应的输入数组的数如果小于当前遍历到的输入数组元素值，
那么就把尾部的元素下标值不断pop出来，
再压入当前输入元素对应的下标值。
然后再从等于滑动窗口大小的位置继续遍历输入数组。
首先把index数组的头元素下标值对应输入数组值压入输出数组。
同样的，如果index数组里面含有元素而且元素后面的下标值对应的输入数组的数如果小于当前遍历到的输入数组元素值，
那么就把尾部的元素下标值不断pop出来，
同时，如果index数组内有元素，而且当一个数字的下标与当前处理的数字的下标只差大于或等于滑动窗口的大小时，
这个数字已经从窗口中画出，可以从队列中删除了，再压入当前输入元素对应的下标值。
最后还需要在输出数组中append一下index手元素下标对应的输入元素值。
'''
class Solution:
    def maxInWindows2(self, num, size):
        if not num or size <= 0 or len(num)<size:
            return []
        deque = [] #队列
        index = [] #索引

        #寻找并保存前size个数字中的最大值对应索引保存在index中
        for i in range(size):
            #如果当前输入到index数组中的数字对应num小于当前遍历到index数组最后一个数字的元素值，
            # 则pop最后一个数字
            #再将当前索引放进去
            while len(index) > 0 and num[i] > num[index[-1]]:
                index.pop()
            index.append(i)
        #再size到最后一个数字中
        for i in range(size, len(num)):
            #针对每一个滑动窗口
            deque.append(num[index[0]])
            #当前i大于index最大
            #弹出最后一个
            while len(index) > 0 and num[i] >= num[index[-1]]:
                index.pop()
            #如果
            if len(index)>0 and index[0] <= i-size:
                #如果当前index【0】不再当前滑动窗口范围内，将其弹出
                index.pop(0)
            index.append(i)
        deque.append(num[index[0]])
        return  deque

    #运行时间：25ms占用内存：5732k
    def maxInWindows(self, num, size):
        if num == [] or size <= 0 or size >len(num):
            return []
        length = len(num)
        result = []
        for i in range(length-size+1):
            result.append(max(num[i:i+size]))
        return result

S = Solution()
print(S.maxInWindows2([2,3,4,2,6,2,5,1],3))