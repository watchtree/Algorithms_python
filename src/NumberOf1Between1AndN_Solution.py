#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/10 21:27
# software: PyCharm
# question: 整数中1出现的个数
'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）
'''
class Solution:
    #暴力搜索,对每个数字进行字符化进行统计
    def NumberOf1Between1AndN_Solution(self, n):
        counts = 0
        for i in range(1, n+1):
            ones = 0
            strs = str(i)
            for j in strs:
                if j == '1':
                    ones += 1
            counts = counts + ones
        return counts

    #递归分析的方法21ms占用内存：5852k
    # 获取每个维数之间1的总数
    def get_1_dights(self,n):
        if n<=0:
            return 0
        if n==1:
            return 1
        a = 9*self.get_1_dights(n-1)
        b = 10**(n-1)
        current = a + b
        return current + self.get_1_dights(n-1)

    def get_1_nums(self, n):
        if n<10:
            return 1 if n>=1 else 0
        dight = len(str(n))
        low_nums = self.get_1_dights(dight-1)
        high = int(str(n)[0])#最高位数字
        low = n - high*10**(dight-1) #排除最高位数的数字

        if high == 1:
            #最高位1
            high_nums = low + 1 #最高位上1 的个数
            all_nums = high_nums
            #最终结果为前n位9999（n-1）的存在的1 的个数
            #加上最高位为1可能出现的次数
            #加上后n-1位可能出现的1的次数
        else:
            #最高为不为1
            high_nums = 10**(dight-1) #最高为上1的次数，1***最多次数
            all_nums = high_nums + low_nums*(high-1)# 20000-29999中一的个数
        return low_nums + all_nums + self.get_1_nums(low)
        #self.get_1_nums(low)是对应出现1****，后面可能出现的1的个数

    #利用数学规律实现
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:

            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones

n = 2
S = Solution()
m=S.get_1_dights(n)
print(m)
n = 10
S = Solution()
print(S.NumberOf1Between1AndN_Solution(n))
