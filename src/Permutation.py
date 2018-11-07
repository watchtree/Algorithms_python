#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/6 22:06
# software: PyCharm
# question: 字符串的排列

'''

输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
class Solution:

    #递归方法
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charlist = list(ss)
        # charlist.sort()
        pStr = []#最外一层保存所有可能
        for i in range(len(charlist)):
            #对于其中一个来说，pSTr应该将当前字符与递归运算后获得的所有的可能性加上
            if i>0 and charlist[i] == charlist[i-1]:
                continue #考虑重复的字符串，若存在相同，则跳出本次，减少时间
            temp = self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))#将i对应于元素排除时进行递归，获得所有可能的str的list
            for j in temp:
                pStr.append(charlist[i]+j) #将可能出现的list的str每一个都加上当前的字符

        return pStr


    #拓展，生成字符的所有组合
    # 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            pStr.append((charList[i]))
            if i>0 and charList[i] == charList[i-1]:
                continue
            temp = self.group(''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
            pStr = list(set(pStr))
            pStr.sort()
        return pStr

ss = 'acb'
S = Solution()
# print(S.Permutation(ss))
print(S.Permutation(ss))

