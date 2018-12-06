#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/6 7:39
# software: PyCharm
# question: 序列化二叉树
'''
请实现两个函数，分别用来序列化和反序列化二叉树
'''
'''
叉树的序列化，二叉树的序列化就是采用前序遍历二叉树输出节点，
再碰到左子节点或者右子节点为None的时候输出一个特殊字符"#"。
'''
'''
对于反序列化，就是针对输入的一个序列构建一棵二叉树，
我们可以设置一个指针先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，
后移一个数字，继续转化为左子树和右子树。
当遇到当前指向的字符为特殊字符"#"或者指针超出了序列的长度，则返回None，指针后移，继续遍历。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #运行时间：33ms占用内存：5864k
    def Serialize(self, root):
        serializeStr = ""
        if root == None:
           return '#'
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                serializeStr += str(root.val) + ','
                root = root.left
            serializeStr += '#,'#d当上述循环结束时说明遇到了空结点，+#
            root = stack.pop()
            root = root.right
        return serializeStr[:-1] #节选最后一个不要“，”

    def Deserialize(self, s):
        #字符串拆分
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        #根据list和list起始位置设定二叉树起始
        if sp>=len(s) or s[sp] == "#":
            return None, sp+1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp



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
aList = S.Serialize(pNode1)
tree = S.Deserialize(aList)
print(aList)
print(tree.val)
