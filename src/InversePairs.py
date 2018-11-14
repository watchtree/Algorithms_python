#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/14 7:35
# software: PyCharm
# question: 数组中的逆序对
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:

题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5
'''
'''
对数据进行排序，需要交换数组中的元素的次数，但是防止相同大小的元素发生交换
因此需要选择一个稳定的排序方法，记录发生交换的次数。
'''
'''
归并排序
'''
class Solution:
    # v1.0，未完成
    #返回逆序对的数量
    def InversePairs(self, data):
        length = len(data)
        if data == None or length<=0:
            return 0
        #复制数组
        count = self.InversePairsCore(data, data[:], 0, length-1)%1000000007
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        #划分左右
        length = (end-start)//2
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)

        #前半段最后一个数字下标
        i = start+length
        #后半段最后一个数字下标
        j = end

        indexCopy = end
        count = 0
        while i>=start and j>=start+length+1:
            #若果前半段数字 大于后半段，则说明出现逆序对
            if data[i]>data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j-start-length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        while i>=start:

            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j>start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count

    # v2.0
    # AC50%可能是出现相同数字时出现问题
    def InversePairs2(self, data):
        sortdata = sorted(data)
        count = 0
        for i in sortdata:
            pos = data.index(i) #顶为排序后的数字在原序列中的索引位置，统计每一个数字在其之前大于其的个数
            count += pos
            data.pop(pos)#统计往后从原始数组
        return count

a = [1,2,3,4,5,6,7,0]
S = Solution()
print(S.InversePairs(a))