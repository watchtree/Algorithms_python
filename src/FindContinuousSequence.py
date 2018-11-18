#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/18 17:35
# software: PyCharm
# question: 和为S的连续正序列
'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    #穷举法运行时间：28ms占用内存：5728k
    def FindContinuousSequence(self, tsum):
        dicsum = {}
        dicsum[1] = 1
        arrayResult = []
        for i in range(2,tsum):
            for m, n in dicsum.items():
                dicsum[m] = n + i
                if dicsum[m]==tsum:
                    temp = [i for i in range(m,i+1)]
                    arrayResult.append(temp)
            dicsum[i] = i
        return arrayResult

    # append会修改a本身，并且返回None。不能把返回值再赋值给a。
    '''
    设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，
    如果和大于目标值，则从当前和中删除small值，并把small值加一，
    如果和小于目标值，则把big值加一，再把新的big值加入和中。
    如果和等于目标值，就输出small到big的序列，同时把big加一并加入和中，继续之前的操作。
    '''
    # 运行时间：30ms占用内存：5720k
    def FindContinousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum+1)//2
        curSum = small + big
        output = []
        while small < middle: #最少两个数字，所以连续数组小的不可能大于最终值的一半
            if curSum == tsum: #目标等于和值，直接添加相对应序列
                output.append(list(range(small, big+1)))
            while curSum > tsum and small < middle: #如果当前值大于设定值，（不停删除序列中最小值直到相等或者又小于设定值了）
                curSum -= small#从当前和中删除最小的那一个
                small += 1#把small+1
                if curSum == tsum:#如果减去之后符合，添加
                    output.append(list(range(small, big+1)))
                #从整体来说就是删除较小的那个，在
            big += 1#如果所小于设定值/当目标执行添加到和值时，再加big+1就会使当前值偏大
            curSum += big#直接在后面加加一个递进+1的big
        return output


S = Solution()
print(S.FindContinuousSequence(100))

