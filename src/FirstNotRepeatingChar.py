#!/usr/bin/env python
#-*-        `   coding:utf-8 -*-
# author:wttree
# datetime:2018/11/13 22:06
# software: PyCharm
# question：第一次只出现一次的字符
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）
'''
class Solution:

    #利用字典保存的方法运行时间：35ms占用内存：5612k
    def FirstNotRepeatingChar(self, s):
        n = len(s)
        dic = {} #保存只出现一次的字符
        dic2 = {} #保存出现多次的字符
        for i in range(n):
            if s[i] in dic2:
                continue
            if s[i] not in dic:
                dic[s[i]] = i
            else:

                dic.pop(s[i])
                dic2[s[i]] = 1
        if dic == {}:
            return -1
        array = sorted(dic.items(), key = lambda x:(-x[1]), reverse=True)
        return array[0][1]

    #运行时间：27ms占用内存：5732k
    def FirstNotRepeatingChar2(self, s):
        if s == None or len(s) <= 0:
            return -1
        alphabet = {}
        for i in s:
            if i not in alphabet:
                alphabet[i] = 0
            else:
                alphabet[i] += 1
        for i in range(len(s)):
            if alphabet[s[i]] == 0:
                return i
        return -1

a = "googgle"
S = Solution()
print(S.FirstNotRepeatingChar2(a))