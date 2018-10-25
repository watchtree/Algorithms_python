#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/25 13:37
# software: PyCharm
# question: 调整数据的顺序使奇数位于偶数前面

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分
并保证奇数和奇数，偶数和偶数之间的相对位置不变
'''

class Solution:

    #v1.0无法保证奇数于奇数、偶数于偶数之间的相对位置不变
    def reOrderArray(self, array):
        n = len(array)
        i = 0
        j = n-1
        while i<j:
            if array[i] % 2 == 1:
                i += 1
                continue
            if array[j] % 2 == 0:
                j -= 1
                continue

            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        return array

    # v2.0只能保证奇数位置不变
    def reOrderArray2(self, array):
        n = len(array)
        for i in range(n-1):
            if array[i] % 2 == 0:
                j = i+1
                while(j<n and array[j]%2==0):
                    j += 1
                if j == n:
                    return array
                else:
                    array[i], array[j] = array[j], array[i]
        return array

    #v3.0拼接的方法
    def reOrderArray3(self, array):
        n = len(array)
        i = 0
        j = n-1
        array1 = []
        array2 =[]
        for i in range(n):
            if array[i] % 2 == 1:
                array1.append(array[i])
            if array[i] % 2 == 0:
                array2.append((array[i]))
        array1.extend(array2)

        return array1

    #3.1简化版
    def reOrderArray31(self, array):
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right

    #4.0,通过不断的添加删除数字
    def reOrderArray4(self, array):
        n = len(array)
        count = 0
        for i in range(n):
            if array[i-count] % 2 == 0:
                temp = array[i-count]
                array.pop(i-count)
                array.append(temp)
                count += 1
        return array
S = Solution()
# print(S.reOrderArray3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.ReorderOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(S.reOrderArray4([1,2,3,4,5,6,7]))
