#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/13 7:42
# software: PyCharm
# question: 丑数
'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
'''
首先除2，直到不能整除为止，然后除5到不能整除为止，然后除3直到不能整除为止。
最终判断剩余的数字是否为1，如果是1则为丑数，否则不是丑数。
'''

class Solution:

    #时间复杂度过大，依次遍历判定的方法
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return None
        if index ==1 :
            return 1
        i = 1
        j = 2
        while(i<index):
            uglyNumber = j
            while(j>1 and j%2==0):
                j = j//2
                if j == 1:
                    i += 1
                    break
            while(j>1 and j%3==0):
                j = j//3
                if j == 1:
                    i += 1
                    break
            while(j>1 and j%5==0):
                j = j//5
                if j == 1:
                    i += 1
                    break
            j = uglyNumber
            j = j+1
        return uglyNumber


    def GetUglyNumber_Solution2(self, index):
        '''
        空间换时间。
        建立一个长度为n的数组，保存这n个丑数。
        在进行运算的时候，某个位置需要求得丑数一定是前面某个丑数乘以2、3或者5的结果，
        我们分别记录之前乘以2后能得到的最大丑数M2，乘以3后能得到的最大丑数M3，乘以5后能得到的最大丑数M5，
        那么下一个丑数一定是M2，M3，M5中的最小的那一个。
        同时注意到，已有的丑数是按顺序存放在数组中的。
        对乘以2而言，肯定存在某一个丑数T2，排在他之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，
        在他之后的每一个丑数乘以2得到的结果都会太大，我们只需记下这个丑数的位置，
        每次生成新的丑数的时候，去更新这个T2。对于3和5同理。
        '''
        if index <= 0:
            return 0
        if index ==1 :
            return 1
        uglyNumbers = [1]*index#以空间换时间，设定一个丑数排序序列
        nextIndex = 1 #丑数计算的index，设定初始为1
        index2 = 0
        index3 = 0
        index5 = 0 #分别为记录最大丑数2，3，5的序列
        #丑数就是2，3，5因子相乘，只可能出现在相对应的序列，对序列中每一个数字乘2，3，5，进行排序赋给下一个
        #
        while nextIndex <index :
            minVal = min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal

            while uglyNumbers[index2]*2 == uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 == uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 == uglyNumbers[nextIndex]:
                index5 += 1
            nextIndex += 1
        return uglyNumbers[-1]

n = 10
S = Solution()
print(S.GetUglyNumber_Solution(n))
