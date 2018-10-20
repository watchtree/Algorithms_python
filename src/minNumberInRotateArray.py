#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/20 21:53
# software: PyCharm
# question: 旋转数组的最小数字

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:

    #v1.0将非减排序视为递增或者不变的，最小值只可能出现在第一个或者旋转开始的位置
    #663ms 5732k
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray == []:
            return 0
        min = rotateArray[0]
        for i in range(1, len(rotateArray)):
            if rotateArray[i] < min:
                min = rotateArray[i]
                return min
        return min

    #551ms5856k
    def minNumberInRotateArray2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) -1
        minVal = rotateArray[0]

        #判定第一项是否小于最后一项，如果是即为递增，直接返回第一项
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            #利用二分法寻找旋转的点
            while(rear - front)> 1:
                mid = (rear+front)//2
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                elif rotateArray[mid] == rotateArray[front] and rotateArray[front] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal
if __name__ == "__main__":
    Test = Solution()
    print(Test.minNumberInRotateArray2([3, 4, 5, 1, 2]))
    print(Test.minNumberInRotateArray2([1, 2, 3, 4, 5]))
    print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
    print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
    print(Test.minNumberInRotateArray([]))
    print(Test.minNumberInRotateArray([1]))