#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/19 6:46
# software: PyCharm
# question: 重建二叉树

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode(object):
    def __init__(self, elem):
        self.val = elem
        self.lchild = None
        self.rchild = None

class Solution:

    #先序遍历 根节点 左子树 右子树
    def preorder(self,root):
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    #中序遍历 左子树 根节点 右子树
    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.val)
        self.inorder(root.rchild)

    #60ms.6480k
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])

        if set(pre) != set(tin):#一个无序不重复元素集, 基本功能包括关系测试和消除重复元素
            return None
        i = tin.index(pre[0]) #确定先序排列确定根节点位置在中序中确定
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

    #简化36ms 5728k
    def reConstructBinaryTree1(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            flag = TreeNode(pre[0])
            flag.left = self.reConstructBinaryTree1(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
            flag.right = self.reConstructBinaryTree1(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return flag

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    test = Solution()
    newTree = test.reConstructBinaryTree1(pre, tin)
    print(newTree.right.left.val)