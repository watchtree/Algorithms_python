#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/17 9:54
# software: PyCharm
# question: 平衡二叉树
'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
'''
它是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
'''
'''
基于二叉树的深度，再次进行递归。以此判断左子树的高度和右子树的高度差是否大于1，若是则不平衡，反之平衡。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#运行时间：28ms占用内存：5736k
class Solution:
    # def IsBalanced_Solution(self, pRoot):
    #     if pRoot == None:
    #         return True
    #     if pRoot.left == None and pRoot.right == None:
    #         return True
    #     leftHight = 1
    #     rightHight = 1
    #     while(abs(leftHight - rightHight)>=2):
    #         leftList = []
    #         rightList = []
    #         while(pRoot.left):
    def __init__(self):
        self.flag = True #定义类的初始值默认为True进行平衡二叉树检验
    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)#不需要返回值，只需要在计算中更新flag值
        return self.flag
    #因为递归计算中需要返回的时每一节子树的高度，而不是是否为平衡数，所以设定函数返回高度，如果出现左右高度不相同ing，
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = 1 + self.getDepth(pRoot.left)
        right = 1 + self.getDepth(pRoot.right)
        if abs(left - right)>1:
            self.flag = False
        return left if left>right else right

# 运行时间：26ms占用内存：5852k
class Solution2:
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right))+1
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left)-self.getDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution2()
print(S.getDepth(pNode1))