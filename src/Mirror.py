#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/12 9:31
# software: PyCharm

# question：操作给定的二叉树，将其变换为源二叉树的镜像。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        if root.left == None and root.right == None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.Mirror(root.left)
        self.Mirror(root.right)

    #递归最简化版本
    def Mirror2(self, root):
        # write code here
        if root != None:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)

    #非递归实现
    def Mirror3(self, root):
        if root == None:
            return
        stackNode = []
        stackNode.append(root)
        while len(stackNode) > 0:
            nodeNum = len(stackNode)-1
            tree = stackNode[nodeNum]
            stackNode.pop(nodeNum)
            # nodeNum -= 1
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
                # nodeNum += 1
            if tree.right:
                stackNode.append(tree.right)
                # nodeNum += 1
    def Mirror4(self, root):
        if root == None:
            return
        nodeQue = [root]
        while len(nodeQue) > 0:
            curLevel = len(nodeQue)
            count = 0
            while count < curLevel:
                count += 1
                pRoot = nodeQue.pop(0)#弹出数组中的第一项
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.left:
                    nodeQue.append(pRoot.left)
                if pRoot.right:
                    nodeQue.append(pRoot.right)

#生成测试所用树
def cteate():
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

    return pNode1,pNode2,pNode3,pNode4,pNode5,pNode6,pNode7

pNode1,pNode2,pNode3,pNode4,pNode5,pNode6,pNode7 = cteate()
S = Solution()
S.Mirror(pNode1)
print(pNode1.right.left.val)


pNode1,pNode2,pNode3,pNode4,pNode5,pNode6,pNode7 = cteate()
S = Solution()
S.Mirror2(pNode1)
print(pNode1.right.left.val)

pNode1,pNode2,pNode3,pNode4,pNode5,pNode6,pNode7 = cteate()
S = Solution()
S.Mirror3(pNode1)
print(pNode1.right.left.val)

pNode1,pNode2,pNode3,pNode4,pNode5,pNode6,pNode7 = cteate()
S = Solution()
S.Mirror4(pNode1)
print(pNode1.right.left.val)