#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/6 7:29
# software: PyCharm
# question: 把二叉树打印成多汗
'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    #运行时间：22ms占用内存：5856k
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        pNodes = [pRoot]
        while pNodes:
            curResult = []
            nextNodes = []
            for node in pNodes:
                curResult.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            result.append(curResult)
            pNodes = nextNodes
        return result