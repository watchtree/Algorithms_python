#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/12 8:22
# software: PyCharm
# question: 把数组拍成最小的数
'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
class Solution:
    # def PrintMinNumber(self, numbers):
    #     if numbers == None:
    #         return None
    #     if len(numbers) == 1:
    #         return numbers
    #     minNumber = self.array2Number(numbers)
    #     for i in range(len(numbers)):
    #         if i == len(numbers)-1:
    #             temp = self.PrintMinNumber(numbers[:i])
    #         else:
    #             temp = self.PrintMinNumber(numbers[:i] + numbers[i + 1:])
    #
    # def array2Number(self, numbers):
    #     Number = ""
    #     for i in numbers:
    #         Number += str(i)
    #     Number = int(Number)
    #     return Number
    #利用排序转化
    def PrintMinNumber(self, numbers):
        from functools import cmp_to_key#老式的比较函数（comparison function）转换为关键字函数（key function）
        if numbers == None or len(numbers) <= 0:
            return ''
        strList = []
        for i in numbers:
            strList.append(str(i)) #将数字列表转化为字符串列表
        key = cmp_to_key(lambda x,y:int(x+y)-int(y+x)) #设定比较函数
        #lambda x,y:int(x+y)-int(y+x)是一个当前后两个字符拼接大于后前拼接，返回正数，也就是说
        # 比较每两个数字串的拼接的mn和nm的大小，若mn < nm，则m更小，反之n更小，然后把更小的数放入一个新的List中
        #有字符串A和B， A + B < B + A，则A在前；反之B在前
        strList.sort(key=key)#以上key作为比较函数
        return ''.join(strList)

a = [3,32,321]
S = Solution()
print(S.PrintMinNumber(a))