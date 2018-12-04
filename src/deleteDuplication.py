#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/4 7:26
# software: PyCharm
# question: 删除链表中重复的结点
'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #错误
    def deleteDuplicationtest(self, pHead):
        #三个辅助指针
        if pHead == None:
            return None
        preNode = None
        pNode = pHead
        pNext = pNode.next
        if pNext == None:
            return pHead
        while pNext:
            if pNode.val == pNext.val:
                preNode.next = pNext.next

                pNode = pNext.next
                pNext = pNode.next
            else:
                preNode = pNode
                pNode = pNext
                pNext = pNode.next

        return pHead

    # 运行时间：31 ms占用内存：5856k
    def deleteDuplication(self, pHead):
        if pHead == None:
            return
        preHead = None
        pNode = pHead
        #当指针对象不为空
        while pNode != None:
            #设定需要判定删除
            needDelete = False
            nextNode = pNode.next
            #如果前后两个相同，需要进行删除，但是不确定需要上述多少个因此设定needDelete
            if nextNode != None and nextNode.val == pNode.val:
                needDelete = True
            #如果不需要删除，直接前推pNode并将preHead设为pNode的前一个
            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            #如果需要删除，考虑连续重复的结点有几个
            else:
                #while推导知道最后一个为None或者值不为当前结点相同初值的值
                nodeVal = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == nodeVal:
                    pToBeDel = pToBeDel.next
                #在此步得到pToBeDel需要删除的最后一个结点的后一个非相同结点
                if preHead == None:
                    #如果是刚开始，设定直接从删除之后的一段开始
                    pHead = pToBeDel
                    pNode = pToBeDel
                    continue
                else:
                    #断掉中间结点直接相连
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead