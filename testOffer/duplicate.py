#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/30 6:52
# software: PyCharm
# question: 数组中重复的数字
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''
class Solution:
    #建立一个哈希表，这样实在O(n)的时间查找到，但是空间复杂度O(n)
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    #运行时间：28ms占用内存：5724k
    def duplicate(self, numbers, duplication):
        if numbers == []:
            return False
        length = len(numbers)
        dicNum = {}
        for i in numbers:
            if i not in dicNum:
                dicNum[i] = 1
            else:
                duplication[0] = i
                return True
        return False

    #在一个长度为n的数组里的所有数字都在0到n-1的范围内。
    #另外一个空间复杂度为O(1)的算法如下
    # 那么如果数字没有重复，那么当数组排序之后数字i将出现在下标为i的位置，
    # 但是有重复的话，在某个位置j出现的数字将不是j。
    # 我们重排这个数组。从头到尾依次扫描这个数组中的每个数字，
    # 如果下标i不是出现数字i，那么就把数字i和i处的数字进行交换使数字i出现在应该出现的位置，
    # 如果新交换的数字还不是他应该出现的位置，继续交换，直至该处的数字m等于x下标m，
    # 如果在交换的过程中，第i处的位置数字等于第m处的数字，
    # 那么我们就找到了第一个重复的数字，记录这个数字，在从下一个位置继续扫描。
    # 运行时间：25ms占用内存：5624k
    def duplicate2(self, numbers, duplication):
        if numbers == None or len(numbers) <= 0:
            return False
        # for i in numbers:
        #     if i<0 or i>len(numbers)-1:
        #         return False
        #重排
        for i in range(len(numbers)):
            #对序列中每一个数字进行判定
            while numbers[i] != i:#如果说直接当前数字等于序列，直接到下一个序列索引
                #如果不是进行处理
                if numbers[i] == numbers[numbers[i]]:
                    #如果当前序列索引到数值等于与这个数字应该放置的位置的数值是相等的，说明遇到了重复数字
                    duplication[0] = numbers[i]
                    return True
                else:
                    #如果不是，将第i个索引上的数值放置到应该的位置上，知道numbers[i] == i进行下一次循环
                    #或者直到numbers[i] == numbers[numbers[i]]当前数字对应
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
            return False




