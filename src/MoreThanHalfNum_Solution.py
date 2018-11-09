#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/8 7:13
# software: PyCharm
# question: 数组中出现次数超过一半的数字
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
思路未实现
'''
'''
：两种思路。第一种思路，出现次数超过一半的数字，不管如何，必然这个数字位于数组中间的位置，
因此可以采用类似于快排的划分的方法，找到位于数组中间的位置的数字，
然后在顺序检索是否这个数字出现次数超过一半。
第二种思路根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，
因此可以最开始保存两个数值：数组中的一个数字以及它出现的次数，然后遍历，
如果下一个数字等于这个数字，那么次数加一，如果不等，次数减一，
当次数等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，
直到进行到最后，然后再验证最后留下的数字是否出现次数超过一半，
因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数字，但是出现次数不一定超过一半。'''
class Solution:
    #v1.0遍历数组，验证数字中各项数字出现的数字O(n).利用字典的方法
    def MoreThanHalfNum_Solution(self, numbers):
        n = len(numbers)
        counts = {}
        for i in numbers:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] = counts[i] + 1

        counts.values()
        for i, j in counts.items():
            if j>n/2:
                return i
        return 0

    #v1.1与上一个版本近似，利用python自身的函数
    def MoreThanHalfNum_Solution1(self, numbers):
        import collections
        temp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in temp.items():
            if v>x:
                return k
        return 0



    #2.0基于Partition函数的O(n)算法
    #该方法无法权AC，问题转不过来了
    #辅助函数函数Partition，输入数组，长度，起始点，结束点
    def Partition(self, numbers, length, start, end):
        #快排用，对数列中其中一段进行
        #取第一个数字作为基准，设定左边的数字大于基准，右边的数字小于基准

        #初始判定，输入符合课分类的情况，最少两个数字且start和end符合要求
        if numbers == None or length<=0 or start<0 or end>=length:
            return None
        #若就只输入一个，返回对应序列索引值
        if end == start:
            return end
        #设定第一个为基准，leftmark和rightmark左右指针
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end

        #循环
        done = False
        while not done:
            #当左指针小于右指针且左小于基准
            while numbers[leftmark] <= pivotvlue and leftmark <= rightmark:
                leftmark += 1
            # 当左指针小于右指针且右大于基准
            while numbers[rightmark] >= pivotvlue and rightmark >= leftmark:
                rightmark -= 1
            #当上述循环结束时说明左大于基准，右小于基准，对应mark
            #如若此时，说明遍历结束，结束循环
            if leftmark >rightmark:
                done = True
            else:
                #对左右进行交换
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        #将基准点数字与最终交换点
        #因为在循环过程中，当最后相差为1，left和right指针依旧会移动一位，此时才会出现停止，最后将start与小的那个数字进行交换
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark

    #检查输入数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid

    #检查找到中位数的元素是否出现的次数超过所有元素的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times*2 <= length:
            return False
        return True

    #Partition函数，它的作用就是将整个数组分成小于基准值的左边，和大于基准值的右边
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0

        middle = length>>1
        start = 0
        end = length - 1
        index = self.Partition(numbers, length, start, end)
        while index != middle:
            if index>middle:
                end = index-1
                index = self.Partition(numbers, length, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, length, start, end)
        result = numbers[middle]
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result


    #v3.0采用用户“分形叶”思路（注意到目标数 超过数组长度的一半，
    # 对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字。
    # 如果剩下两个，那么这两个也是一样的，就是结果），在其基础上把最后剩下的一个数字或者两个回到原来数组中
    # 将数组遍历一遍统计一下数字出现次数进行最终判断
    def Mas(self, numbers):
        #初始判定与检验
        length = len(numbers)
        if numbers == None or length <= 0:
            return 0
        if length == 1:
            return numbers[0]
        #复制lists
        temp = [i for i in numbers]

        #对不同的数字置为0
        for i in range(length):
            if (temp[i] == 0):
                continue
                #用0进行数字抹除，所以遇到0时直接跳出本次循环
            for j in range(i, length):
                if temp[i] != temp[j] and temp[j] != 0:
                    temp[i] = 0
                    temp[j] = 0  # 抹去不同的数字
                    break
        #统计第一个经过多次删除后不为0的值
        result = 0
        for i in range(length):
            if temp[i] != 0:
                result = temp[i]
                break
        #统计验证是否符合要求


        times = 0
        for i in range(length):
            if result == numbers[i]:
                times += 1
        if times * 2 < length:
            return 0
        return result




numbers = [2,3,2,2,2,1]
numbers = [4,2,1,4,2,4]
S = Solution()
i = S.MoreThanHalfNum_Solution(numbers)
print(i)