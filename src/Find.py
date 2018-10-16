#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/16 12:50
# software: PyCharm
# question: 二维数组中的查找

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

import time

#v1.0遍历的方法检查样本中的整数
class Solution:
    def Find(self, array, target):
        if array == []:
            return False
        m = len(array)
        n = len(array[0])

        for i in range(m):
            for j in range(n):
                if array[i][j] == target:
                    return True
                if array[i][j] > target:
                    break
        return False

    #v2.0修正
    '''
    查找方式从**右上角**开始查找
    从右上角开时原因实在元素大于target时，同样保证该元素下的元素值都大于target，需要左移
    如果当前元素大于target, 左移一位继续查找
    如果当前元素小于target, 下移一位继续查找
    进行了简单的修改, 可以判定输入类型为字符的情况
    
    #如果假设从左上角查询， 其当判定该元素小于目标需要右移动时，无法保证之前的一列全部不为target
    '''
    def Find2(self, array, target):
        if array == []:
            return False
        rawnum = len(array)
        colnum = len(array[0])

        #改为while循环方便在中间及逆行i j的移动
        i = colnum - 1
        j = 0

        while i >= 0 and j < rawnum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            elif array[j][i] == target:
                return True
        return False

    #v3.0附加一些字符串之类
    def Find3(self, array, target):
        if array == []:
            return False
        rawnum = len(array)
        colnum = len(array[0])

        #判断输入
        if type(target) == float and type(array[0][0]) == int:
            if int(target) == target: #浮点数判定相等一般来说判定两个数的差值是否小于一个特别小的数字
                return False
            target == int(target)
        elif type(target) == int and type(array[0][0]) == float:
            target == float(target)
        # elif type(target)   type(array[0][0]):
        #     return False

        #改为while循环方便在中间及逆行i j的移动
        i = colnum - 1
        j = 0

        while i >= 0 and j < rawnum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            elif array[j][i] == target:
                return True
        return False

if __name__ == "__main__":
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array2 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    # array3 = [['a', 'b', 'c'],
    #           ['b', 'c', 'd']]
    array4 = [[62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
              [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
              [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
              [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
              [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
              [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]]

    findtarget = Solution()
    # print(findtarget.Find3(array, 10))
    # print('###########')
    # print(findtarget.Find3(array, 30))
    # print('###########')
    # print(findtarget.Find3(array, 13.0))
    # print('###########')
    # print(findtarget.Find(array, ''))
    # print('###########')
    print(findtarget.Find(array2, 10))
    print('###########')
    # print(findtarget.Find(array3, 'b'))
    # print(findtarget.Find(array3, 'b'))
