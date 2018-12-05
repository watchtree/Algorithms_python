#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/5 8:11
# software: PyCharm
# question: 二叉树的下一个结点
'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针
'''
'''
三种情况：
当前节点有右子树的话，当前节点的下一个结点是右子树中的最左子节点；
当前节点无右子树但是是父节点的左子节点，下一个节点是当前结点的父节点；
当前节点无右子树而且是父节点的右子节点，则一直向上遍历，直到找到最靠近的一个祖先节点pNode，pNode是其父节点的左子节点，那么输入节点的下一个结点就是pNode的父节点。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    # 运行时间：31ms占用内存：5752k
    def GetNext(self, pNode):
        if pNode == None:
            return
        pNext = None

        #有右子树
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            pNext = pRight
        elif pNode.next != None:
            pCurrent = pNode
            pParent = pCurrent.next
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pCurrent.next
            pNext = pParent
        return pNext
