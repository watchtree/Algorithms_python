#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/26 22:34
# software: PyCharm
# question: 圆圈中最后剩下的数
'''
首先,让小朋友们围成一个大圈。
然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....
直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        #运行时间：996ms占用内存：5856k
        if n<1 or m<1:
            return -1
        List = [i for i in range(n)]
        cur = 0
        tempm = m
        while(tempm!=0 and len(List)!=1):
            if cur >= len(List):
                cur = 0
            tempm = tempm - 1
            if (tempm == 0):
                List.pop(cur)
                tempm = m
                continue
            cur = cur + 1
        return List[0]

    #d递归数学方法运行时间：30ms占用内存：5864k
    def LastRemaining_Solution2(self, n, m):
        if n<1 or m<1:
            return -1
        remainIndex = 0
        for i in range(1, n + 1):
            remainIndex = (remainIndex + m) % i
        return remainIndex

S = Solution()
print(S.LastRemaining_Solution2(5,1))
