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
'''
 采用二分法解答这个问题，
mid = low + (high - low)/2
需要考虑三种情况：
(1)array[mid] > array[high]:
出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。
low = mid + 1
(2)array[mid] == array[high]:
出现这种情况的array类似 [1,0,1,1,1] 或者[1,1,1,0,1]，此时最小数字不好判断在mid左边
还是右边,这时只好一个一个试 ，
high = high - 1
(3)array[mid] < array[high]:
出现这种情况的array类似[2,2,3,4,5,6,6],此时最小数字一定就是array[mid]或者在mid的左
边。因为右边必然都是递增的。
high = mid
注意这里有个坑：如果待查询的范围最后只剩两个数，那么mid 一定会指向下标靠前的数字
比如 array = [4,6]
array[low] = 4 ;array[mid] = 4 ; array[high] = 6 ;
如果high = mid - 1，就会产生错误， 因此high = mid
但情形(1)中low = mid + 1就不会错误 
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
    '''
    二分查找的变形，注意到旋转数组的首元素肯定不小于旋转数组的尾元素，设置中间点。
    如果中间点大于首元素，说明最小数字在后面一半，如果中间点小于尾元素，说明最小数字在前一半。
    依次循环。同时，当一次循环中首元素小于尾元素，说明最小值就是首元素。
    但是当首元素等于尾元素等于中间值，只能在这个区域顺序查找。
    '''
    def minNumberInRotateArray2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) -1
        minVal = rotateArray[0]

        #v2.0判定第一项是否小于最后一项，如果是即为递增，直接返回第一项
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
                    for i in range(front, rear):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal


        #v3.0实例方法572ms 9032k
    def minNumberInRotateArray3(self, rotateArray):
            if len(rotateArray) == 0:
                return 0
            front = 0
            rear = len(rotateArray) - 1
            midIndex = 0
            while rotateArray[front] >= rotateArray[rear]:
                if rear - front == 1:
                    midIndex = rear
                    break
                midIndex = (front+rear)//2
                if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                    return self.MinInOrder(rotateArray, front, rear)
                if rotateArray[midIndex] >= rotateArray[front]:
                    front = midIndex
                elif rotateArray[midIndex] <= rotateArray[rear]:
                    rear = midIndex
            return rotateArray[midIndex]

    #递归求最小数字序列数字
    def MinInOrder(self, array, front, end):
        result = array[0]
        for i in array[front: end+1]:
            if i<result:
                result = i
        return result

if __name__ == "__main__":
    Test = Solution()
    print(Test.minNumberInRotateArray3([3, 4, 5, 1, 2]))
    print(Test.minNumberInRotateArray2([1, 2, 3, 4, 5]))
    print(Test.minNumberInRotateArray3([1, 1, 1, 0, 1]))
    print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
    print(Test.minNumberInRotateArray([]))
    print(Test.minNumberInRotateArray([1]))