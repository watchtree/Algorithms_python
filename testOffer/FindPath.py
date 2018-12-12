#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/4 7:53
# software: PyCharm
# question: 二叉树中和为某一值的路径
'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径

    #递归
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root.left == None and root.right == None:
            if expectNumber == root.val:
                return [[root.val]] #将数组保存在列表中
            else:
                return []
        stack = []
        leftstack = self.FindPath(root.left, expectNumber - root.val)
        for i in leftstack:
            #从返回的列表中读取数组，若返回【】 则此部不存咋。
            #若存在返回值则可以数组中添加当前val形成数组
            i.insert(0, root.val)
            stack.append(i)
        rightstack = self.FindPath(root.right, expectNumber - root.val)
        for i in rightstack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    #v2.0只能保证按顺序从左到右，不能如题说是保证数组长度达的数组靠前
    def FindPath2(self, root, expectNumber):
        if not root:
            return []
        if root.left == None and root.right == None:
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []
        a = self.FindPath2(root.left,expectNumber-root.val) + self.FindPath2(root.right, expectNumber - root.val)
        return [[root.val] + i for i in a]#给每一个传递来的数组都加上[root.val]形成序列
        #i for i in a直接生成序列
pNode1 = TreeNode(10)
pNode2 = TreeNode(16)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode3.left = pNode4
pNode3.right = pNode5


S = Solution()
print(S.FindPath2(pNode1, 26))
