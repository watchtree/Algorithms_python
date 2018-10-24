#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/24 8:25
# software: PyCharm
# question: 二进制中1的个数
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
'''
'''
注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，那么二进制数中的1的个数就会减少一个
因此可以利用一个循环，使得 n = n&(n-1) ，计算经过几次运算减少到0，就是有几个1。
注意：书中给了另外两种方法，分别是原始n左移一位和右移一位的方法，因为Python不会出现整数溢出的情况，这里就不再考虑着两种方法。
扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中有且只有一个1，那么这个数n会有 n&(n-1) == 0。或者求两个整数m和n需要改变m二进制中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。
'''
'''
原码：将一个整数，转换成二进制，就是其原码。
               如单字节的5的原码为：0000 0101；-5的原码为1000 0101。

　反码：正数的反码就是其原码；负数的反码是将原码中，除符号位以外，每一位取反。
               如单字节的5的反码为：0000 0101；-5的反码为1111 1010。

　补码：正数的补码就是其原码；负数的反码+1就是补码。
               如单字节的5的补码为：0000 0101；-5的原码为1111 1011。

　　在计算机中，正数是直接用原码表示的，如单字节5，在计算机中就表示为：0000 0101。
                          负数用补码表示，如单字节-5，在计算机中表示为1111 1011。
'''
class Solution:
    #v1.0只符合整数为正数的情况
    #负数会出现无限循环，负数在计算机中是用补码表示的，最高位是1，在右移的过程中，高位都是用1来填补的
    def NumberOf11(self, n):
        count = 0
        while n:#循环
            if n&1 == 1: #按位与，检验n最后一个是否为1
                count += 1
            n = n>>1 #右移
        return count

    def NumberOf12(self, n):
        count = 0
        while n:
            count += 1
            n = (n - 1) & n #每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0
            #原理：保证其他位置不变，只改变最后那个1将其变为0
        return count


    #python v2.0利用转化将负数转化为无符号整数进行判定
    def NumberOf21(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff #技巧：在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
        while n:
            if n&1 == 1:
                count += 1
            n = n>>1
        return count

    def NumberOf22(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff #技巧：在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
        while n:
            count += 1
            n = (n - 1) & n  # 每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0
            # 原理：保证其他位置不变，只改变最后那个1将其变为0
        return count

    def NumberOf3(self, n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])
if __name__ == "__main__":
    S = Solution()
    # print(S.NumberOf1(-1))
    # print(S.NumberOf2(-1))
    print(S.NumberOf3(123))
    print(bin(123).count('1'))
    #返回一个整数 int 或者长整数 long int 的二进制表示。
    print(S.NumberOf3(-123))
    print(bin(-123&0xffffffff).count('1'))
