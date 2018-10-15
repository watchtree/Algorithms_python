#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/15 10:47
# software: PyCharm
# question：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。要求：使得时间复杂度都是O（1）


# 此种方法在栈中输入数字时，即利用minStack总是将最小的数字放入其中最后一个
# 时间复杂度应为O（1）为了达到这种效果，对类多加一个minstack，表示在相应的stack中最小的放在最后一位
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node <self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        if self.stack == None or self.minStack ==[]:
            return None
        self.minStack.pop() #默认弹出最后一个元素,弹出后默认最后一个数字同样为最小值
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    #首先时间复杂度要求为O（1），此处采用索引的方法得到相应最小值
    def min(self):
        return self.minStack[-1]

if __name__ == '__main__':

    S = Solution()
    S.push(3)
    S.push(4)
    S.push(2)
    S.push(1)
    print(S.min())
    S.pop()
    print(S.min())
    S.pop()
    print(S.min())