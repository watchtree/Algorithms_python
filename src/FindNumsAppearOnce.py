#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/17 12:40
# software: PyCharm
# question: 数组中只出现一次的数字
'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
检查数组中一个只出现奇数次，其他都只出现偶数次的，直接依次异或。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    # 运行时间：29 ms占用内存：5752k
    def FindNumsAppearOnce(self, array):
        length = len(array)
        if length < 2:
            return None
        dic = {}
        for i in range(length):
            if array[i] not in dic:
                dic[array[i]] = 1
            else:
                dic.pop(array[i])
        result = []
        for m, n in dic.items():
            result += [m]
        return result
    #运行时间：27ms占用内存：5624k

    def FindNumsAppearOnce2(self, array):
        length = len(array)
        if length < 2:
            return None
        dic = {}
        for i in range(length):
            if array[i] not in dic:
                dic[array[i]] = 0
            else:
                dic[array[i]] += 1
        result = []
        for m, n in dic.items():
            if n==0:
                result += [m]
        return result
    '''
    异或:如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。a⊕b = (¬a ∧ b) ∨ (a ∧¬b)
    任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数
    '''
    '''
    数组中出了两个数字之外，其他数字都出现两次，
    那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵消掉，
    那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。
    我们找到结果数字中最右边为1的那一位i，然后一次遍历数组中的数字，
    如果数字的第i位为1，则数字分到第一组，数字的第i位不为1，则数字分到第二组。
    这样任何两个相同的数字就分到了一组，而两个不同的数字在第i位必然一个为1一个不为1而分到不同的组，
    然后再对两个组依次进行异或操作，最后每一组得到的结果对应的就是两个只出现一次的数字。
    '''
    # 运行时间：27ms占用内存：5732k
    def FindNumsAppeaOnce3(self, array):
        if array == None or len(array) <= 0:
            return []
        resultExcluesiveOr = 0
        for i in array:
            resultExcluesiveOr ^= i
        #resultExcluesiveOr为数字依次异或得到的数字，存在两个不同的数字，则数字不为零
        indexOf1 =self.FindFirstBitIs1(resultExcluesiveOr)#得到索引值，在这一位上两个不同的数字也不同
        num1, num2 = 0, 0
        for j in range(len(array)):
            if self.IsBit1(array[j], indexOf1):#以indexOf1对不同数字进行区分，划分到了不同的组当中，相同的数字在同一个组
                num1 ^= array[j]#进行异或，相同数字为0，保留不同数字
            else:
                num2 ^= array[j]
        return [num1, num2]
    def FindFirstBitIs1(self, num):
        #输入异或结果
        indexBit = 0
        while num&1 ==0 and indexBit <= 32:#num&1 ==0判定最后一位是否为零，若位零，则索引index+1
            indexBit += 1
            num = num >> 1 #右移动一位
        return indexBit#得到一个序列值

    def IsBit1(self, num, indexBit):
        num = num>>indexBit
        return num&1

a = [2,4,3,6,3,2,5,5]
S = Solution()
print(S.FindNumsAppeaOnce3(a))