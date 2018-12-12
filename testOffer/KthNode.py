#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/7 10:09
# software: PyCharm
# question: 二叉搜索树的第k个结点
'''
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
'''
'''
二叉排序树
它或者是一棵空树，
或者是具有下列性质的二叉树： 
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树
'''
'''
中序遍历(左根右)输出一个序列，然后找到序列中第k个数即可。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    #运行时间：29ms占用内存：5728k
    def KthNode(self, pRoot, k):
        global result
        result = []
        if k == 0 or pRoot == None:
            return None
        self.inOrder(pRoot)
        if len(result) < k:
            return None
        return result[k - 1]
    def inOrder(self, root):
        if not root:
            return []
        self.inOrder(root.left)
        result.append(root)
        self.inOrder(root.right)
class Solution2:
    def __init__(self):
        self.treeNode = []
    def inOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.inOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.inOrder(pRoot.right)
    def KthNode(self, pRoot, k):
        if k <= 0 or not pRoot:
            return None
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k-1]


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

print(S.KthNode(pNode1, 1))