#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/16 8:55
# software: PyCharm
# question: 二叉树的深度
'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #递归算法，统计最长路径
    # 运行时间：46ms占用内存：6084k
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if left<right:
            return right+1
        else:
            return left+1

    # 运行时间：29ms占用内存：5732k
    #非递归方法， 利用一个list存储每一层的节点，将每一层下左右每个节点更新到b中，最终将a更新为b进行下一轮迭代
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        a = [pRoot]#用于存储每一层存在的节点，多进行一次向下存储则+1
        d = 0
        while a:
            b =[]
            for node in a:
                if node.left:
                    b.append(node.left)
                if node.right:
                    b.append(node.right)
            a = b
            d = d+1
        return d