#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/27 20:24
# software: PyCharm
# question: 输入一个链表，反转链表后，输出新链表的表头
'''
需要注意三个问题：输入的链表头指针为None或者整个链表只有一个结点时，反转后的链表出现断裂，
返回的翻转之后的头节点不是原始链表的尾结点。因此需要引入一个翻转后的头结点，
以及一个指向当前结点的指针，一个指向当前结点前一个结点的指针，一个指向当前结点后一个结点的指针，防止出现断裂。
推广：递归实现反转链表
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 非递归方法
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while(pNode != None):
            pNext = pNode.next

            if pNext == None:
                pReversedHead = pNode #在循环中不停的将反转链表的表头改为最后一个

            pNode.next = pPrev #将相对应每个对象指向上一个
            pPrev = pNode #保存作为前一个对象
            pNode = pNext #更新Node为下一个

        return pReversedHead

    #递归方法
    def ReverseList1(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseList1(pHead.next) #递归到最后一个会返回最后一个的node
            pHead.next.next = pHead #设定将链表反向，pHead.next为最后一个当前node，设定反转
            pHead.next = None
            return pReversedHead