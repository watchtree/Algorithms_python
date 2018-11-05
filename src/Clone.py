#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/5 9:57
# software: PyCharm
# question: 复杂链表的复制
'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
'''
注意链表结点进行复制的时候，不能简单地写作 pCloned = pNode，
这样的话之后对pCloned的操作也会作用在pNode上面，导致操作循环往复。
需要重新定一个pCloned = ListNode(0)，然后对结点的.val .next .random 进行设置。
同时，在将复制的结点的random指向原始链表结点的random的next的时候，
需要先判断一下，原始链表结点的next是否为None，不为None再指向。
'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    #复制链表的每个节点，将复制的结点链接在其原始结点的后面,形成结点、复制结点、结点、复制结点的形式
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            # pCloned = pNode会导致在之后的对pNode.next = pCloned pNode = pCloned.next循环往复

            pCloned = RandomListNode(0)#设定一个新的结点并对其进行设置
            pCloned.label = pNode.label
            pCloned.next = pNode.next

            pNode.next = pCloned
            pNode = pCloned.next

    #将复制后的链表中的渎职结点的random指针链接到被复制结点random指针的后一个结点
    #对堆积特殊指针进行处理random，检查每一个结点是否由random指针指向，若存在将复制产生结点的random指向，原本
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next#pCloned是由上一步函数形成的复制结点
            if pNode.random != None:
                pCloned.random = pNode.random.next #如果随机不为None，则将复制下一个放入随机
                # 将复制的结点的random指向原始链表结点的random（该为本身的结点）的next（应该指向的复制结点）
            pNode = pCloned.next#对经过复制的下一个结点进行操作

    #拆分链表，将原始链表的结点组成新的链表，复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = pCloneNode = pNode.next#复制链表的起始结点为当前初始head的下一个为复制的
        pNode.next = pCloneHead.next #跳过复制的一个，将原本的连接接上
        pNode = pNode.next
        while pNode:
            pCloneNode.next = pNode.next #复制后的下一个就为当前下一个
            pCloneNode = pCloneNode.next #对复制结点更新到下一个，为下一个结点的复制结点
            pNode.next = pCloneNode.next #将本身原本的连接解上
            pNode = pNode.next

        return pCloneHead



node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)

