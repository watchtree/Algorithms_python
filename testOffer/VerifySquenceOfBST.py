#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/3 7:03
# software: PyCharm
# question: 二叉搜索树的后续遍历序列
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
'''
根据后序遍历的性质，在二叉树中，先左后右再根，即首先遍历左子树，然后遍历右子树，最后访问根结点。
前序遍历根左右
中序遍历左根右
后序遍历左右根
二叉搜索树的性质： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
尾元素必定是树的根，同时小于尾元素的值是左子树，大于尾元素的值为右子树，
且序列前半部分均小于尾元素，后半部分均大于尾元素（如果同时存在左右子树的话），
可以将序列划分左子树序列和右子树序列，然后递归比较每一段均满足此性质。
可以减少递归深度的办法：某段的元素个数如果<=3，则返回True；
某整段的最小元素不小于尾元素或者整段的最大元素不大于尾元素，说明仅有左子树或者右子树，返回True。
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]#后序遍历最后一个为根节点
        length = len(sequence)
        index = 0
        while(sequence[index]<root):
            index += 1
        #检验在序列中小于root的部分，若出现大于，即可以break保存index作为左右子树的区分
        #若root前所有元素小于root时，结束时index = length-2
        #若将下面一个循环起始点改为index就不对了
        for j in range(index+1, length-1):
            if sequence[j] < root:
                return False
        #检查右子树部分，若存在小于root，则返回False

        left = True
        if index>0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index<length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])
        return right and left

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))

