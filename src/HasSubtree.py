#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/31 22:25
# software: PyCharm
# question: 树的子结构
'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #辅助函数，利用递归方法判定两个数是否相同,但是不适用于该题中的情况，因为其是判定在输出输出相同部分相同
    def isSameTree(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot2 == None:
            return False
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.isSameTree(pRoot1.left, pRoot2.left) and self.isSameTree(pRoot1.right, pRoot2.right)

    #辅助函数，对相同val节点下相对应位置进行比较
    #因为检验时树1包含树2，因此当递归到pRoot2==None说明在次节点之前树相同他，不进行之后的判定
    #如果颠倒顺序，会先判断pRoot1是否为None， 其实这个时候pRoot2的节点已经完全检查过确认相等了
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)

    #主函数，判定是否包含遇到相同的节点
    def HasSubtree(self, pRoot1, pRoot2):
        #默认为不相同
        result = False

        if pRoot1 != None and pRoot2 != None:
            #若节点相同且当前对应节点值相同
            if pRoot1.val == pRoot2.val:
                #进行判定对应节点下是否相同
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                #若不相同则进行递归，先左树的左节点递归
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                #如此时判定依旧为False。将右树输入递归
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    #v2简化
    def HasSubTree2(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.DoesTree1haveTree2(pRoot1,pRoot2) or self.HasSubTree2(pRoot1.left, pRoot2) or self.HasSubTree2(pRoot1.right, pRoot2)

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubTree2(pRoot1, pRoot8))