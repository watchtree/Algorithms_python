#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/30 7:51
# software: PyCharm
# question: 构建乘积数组
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
'''
class Solution:
    #运行时间：24ms占用内存：5732k
    def multiply(self, A):
        B = []
        length = len(A)
        for i in range(length):
            temp = 1
            for j in range(length):
                if i == j:
                    continue
                temp = temp*A[j]
            B.append(temp)
        return B

    #分两步进行
    # 运行时间：28ms占用内存：5728k
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        length = len(A)
        aList = [1]*length
        for i in range(1, length):
            aList[i] = aList[i-1]*A[i-1]
        #aList乘积数组，依次相乘放入aList中
        #此时最后一个数字即为前n-1个数字相乘的结果。
        #因此从倒数第二个数字开始处理，乘后面未乘的数字
        temp = 1
        for i in range(length-2, -1 ,-1):
            temp = temp * A[i+1]
            aList[i] *= temp
        return aList
A = [1,2,3,4,5]
S = Solution()
print(S.multiply(A))