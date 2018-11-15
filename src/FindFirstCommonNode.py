#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/15 10:10
# software: PyCharm
# question: 两个链表的第一个公共节点
'''
输入两个链表，找出它们的第一个公共结点。
'''
'''
首先依次遍历两个链表，记录两个链表的长度m和n，
如果 m > n，那么我们就先让长度为m的链表走m-n个结点，
然后两个链表同时遍历，当遍历到相同的结点的时候停止即可。
对于 m < n，同理。
'''
'''
首先需要明确一点，如果两个链表有公共节点，那么从第一个公共节点开始，直到链表结束，
这段链表的长度N对两个链表来说长度是一致的，且公共链表必定是从距离两个链表尾向前N（公共部分的节点个数）个节点的位置的下一位置开始的。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:

    #辅助函数，查找链表长度
    def getListLength(self, pHead):
        nlength = 0
        while pHead!=None:
            pHead = pHead.next
            nlength += 1
        return nlength

    #运行时间：29ms占用内存：5856 k
    # 时间复杂度O(M + N)
    def FindFirstCommonNode(self, pHead1, pHead2):
        nlength1 = self.getListLength(pHead1)
        nlength2 = self.getListLength(pHead2)

        if nlength1>nlength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1
        nlengthDiff = abs(nlength1-nlength2)
        for i in range(nlengthDiff):
            pListHeadLong = pListHeadLong.next
        while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
            pListHeadShort = pListHeadShort.next
            pListHeadLong = pListHeadLong.next

        pFirstCommonNode = pListHeadLong
        return pFirstCommonNode

    # 运行时间：30ms占用内存：5856k
    #时间复杂度O(MlogM)，空间复杂度O(max(M,N))
    def FindFirstCommonNode2(self, pHead1,pHead2):
        list1 = []
        node1 = pHead1
        node2 = pHead2
        while node1:
            list1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next

    # 运行时间：31ms占用内存：5752k
    # 时间复杂度O(M + N)
    # 不需要额外空间
    '''
    如果两条链表的长度相同，那么第一遍到尾部前就能找到第一个公共节点（如果有的话）。
    如果两条链表长度不同，本来在较短链表的游标转移到较长的链表上，当本来在较长链表上的游标到达尾部并转到较短链表的时候，两个游标离尾部的距离相同，所以第二遍一定能找到公共节点（如果有的话）
    '''
    def FindFirstCommonNode3(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        ptr1 = pHead1
        ptr2 = pHead2
        while ptr1 != ptr2:
            if ptr1 and ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
                continue
            if ptr1 == None:
                ptr1 = pHead2
            if ptr2 == None:
                ptr2 = pHead1
        if ptr1:
            return ptr1
        else:
            return None