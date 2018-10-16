#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/17 7:35
# software: PyCharm
# question: 替换空格
'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution:

    #进行遍历，创建辅助list，时间复杂度O（n） 21ms 5736k
    def replaceSpace(self, s):
        string = list(s)
        stringReplace = []
        for i in string:
            if i == ' ':
                stringReplace.append("%20")
            else:
                stringReplace.append(i)
        return "".join(stringReplace)

    #创建新的字符串进行替换20ms 5856k
    def replaceSpace1(self, s):
        tempstr = ''
        if type(s) != str:
            return
        for i in s:
            if i == ' ':
                tempstr += '%20'
            else:
                tempstr += i
        return tempstr

    #简单代码替换24ms 5716k
    def replaceSpace(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

if __name__ == '__main__':
    s = 'we are happy'
    test = Solution()
    print(test.replaceSpace(s))
    # print(test.replaceSpace2(s))
    # print(test.replaceSpace3(s))
