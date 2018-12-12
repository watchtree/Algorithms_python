#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/6 7:16
# software: PyCharm
# question: 二叉搜索树与双向链表
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
按照左右子树分治，递归实现。根的左边连接左子树的最右边结点，右边连接右子树的最左边结点
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    #递归、中序遍历
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        #处理左子树，会将左子树形成一个顺序排列的序列链表
        self.Convert(pRootOfTree.left)
        #递归，当递归到此步时，已经达到最左边的点，但是
        left = pRootOfTree.left
        #连接跟与左子树最大结点
        if left:
            while left.right:
                left = left.right#因为循环递归的原因，经过处理之后的左子树显然最右的是最大的，因此找到那一个，与当前结点双向连接
            pRootOfTree.left, left.right = left, pRootOfTree#形成双向链表

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree

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
newList = S.Convert(pNode1)
print(newList.val)