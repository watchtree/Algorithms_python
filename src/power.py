#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/25 12:37
# software: PyCharm
# question: 数值的整数此方
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
'''
需要注意的地方:
当指数为负数的时候
当底数为零切指数为负数的情况
在判断底数base是不是等于0的时候,不能直接写base==0, 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
'''
class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            temp = 1.
            for i in range(-exponent):
                temp = temp/base
            return temp
        elif exponent == 0:
            return 1
        else:
            temp = 1.0
            for i in range(exponent):
                temp = temp*base
            return temp
    def power2(self, base, exponent):
        #递归方法，利用二分相乘，减少了计算次数
        '''
        当n为偶数, a^n = a^(n/2) * a^(n/2)
        当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
        利用右移一位运算代替除以2
        利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
        优化代码速度
        '''
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1 / base


        result = self.Power(base, exponent >> 1) #类似于二分求相乘的方法求平均
        result *= result

        #利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
        if (exponent & 0x1) == 1:
            result *= base

        return result


S = Solution()
print(S.power2(5, -2))