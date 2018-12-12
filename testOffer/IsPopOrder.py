#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/15 11:41
# software: PyCharm
# question: 栈的压入、弹出序列

'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
栈结构 理解:栈，这个“后进先出(Last In First Out)” 数据结构应该都不陌生。
如果 a、b、c 依次入栈，然后出栈，那么出栈顺序是 c、b、a；
如果 a 入栈然后出栈、b 入栈出栈、c 入栈出栈，那么出栈顺序是 a、b、c。
如果只是强调 a、b、c 的入栈顺序，而不强调具体的出栈顺序，那么 cba 和 abc 都可以是出栈顺序，acb、bac 和 bca 也都可以，
而 cab 是不可以的：因为 c 首先出栈说明 a b 在栈中，c 出栈后其他出栈顺序只能是 ba 而不可能是 ab
'''

class Solution:

    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False

        stack = []
        for i in pushV:
            stack.append(i)
            if stack[-1] != popV[0]:
                continue
            else:
                stack.pop()
                popV.pop(0)
        while len(stack) > 0 and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        if len(stack) == 0:
            return True
        else:
            return False

    #优化版
    def IsPopOrder2(self, pushV, popV):
        if pushV == [] or popV ==[]:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True

if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    S = Solution()
    print(S.IsPopOrder2(pushV, popV))
