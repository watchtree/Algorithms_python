#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/6 6:59
# software: PyCharm
# question： 按之字形打印二叉树
'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''
按之字形顺序打印二叉树需要两个栈。
我们在打印某一行节点时，拔下一层的子节点保存到相应的栈里。
如果当前打印的奇数层，则先保存左子节点再保存右子节点到第一个栈里；
如果当前打印的是偶数层，则先保存右子节点再保存左子节点到第二个栈里。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #运行时间：22ms占用内存：5728k
    def Print(self, pRoot):
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        right = True
        while nodes:
            curStack, nextStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
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
aList = S.Print(pNode1)
print(aList)

