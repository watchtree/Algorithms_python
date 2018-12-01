#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/1 8:33
# software: PyCharm
# question: 正则表达式匹配
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):

        if s == pattern:
            return True
        if s != "" and pattern == "":
            return False

        #当字符串为空时，有下列可能性
        elif s == "":
            if len(pattern) == 1:
                return False
            #若上式不满足，则说明patten长度大于2且第第二个为*,可以任意匹配，进行迭代，看patten后面的字符
            if pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return self.match(s, pattern[1:]) #递归方法

        if len(pattern) == 1:
            if len(s) == 1 and pattern[0] == ".":
                return True
            else:
                return False

        #当字符串不为空时
        #当patten大于等于2且第二个不为*时，相当于对于第一位对比只有可能相等或者”。“
        if len(pattern) >= 2:
            if pattern[1] == "*":
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern)
                else:
                    return self.match(s[1:], pattern[2:])
            else:
                if s[0] == pattern[0] or pattern[0] == ".":
                    return  self.match(s[1:], pattern[1:])
                else:
                    return self.match(s, pattern[1:])

        return False

    #主要是对于星号，只有*前一个是随便可以放随意个数字的维数
    def match2(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == "*":
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == "."):
                return self.match2(s, pattern[2:]) or self.match2(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        #对于星号前第两个，一对一对应消除
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == "."):
            return self.match2(s[1:], pattern[1:])
        else:
            return False


s = Solution()
print(s.match("aaa","a.a"))