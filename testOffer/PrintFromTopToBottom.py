#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/2 9:09
# software: PyCharm
# question: 从上往下打印二叉树
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印
思路是用arraylist模拟一个队列来存储相应的TreeNode
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        #辅助空间，保存一行的节点按顺序
        queue = []
        if not root:
            return []
        result = []
        queue.append(root)
        #将根节点添加
        while len(queue)>0:
            currentRoot = queue.pop(0)#弹出首个节点保存在辅助数组中
            result.append(currentRoot.val) #提取值
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
result = S.PrintFromTopToBottom(pNode1)
print(result[1].val)