#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/3 7:41
# software: PyCharm
# question：链表中环的入口结点
'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
'''
寻找链表中环的入口结点主要分成三个步骤：
首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；
然后从相遇的地方设置一个指针向后遍历并记录走的步数，
当这个指针重新指到开始的位置的时候，当前对应的步数就是环中结点的数量k；
然后设置两个指针从链表开始，第一个节点先走k步，
然后第二个指针指到链表的开始，两个指针每次都向后走一步，两个指针相遇的位置就是链表的入口。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 运行时间：29ms占用内存：5848k

    #首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；
    #因为在非环部分，慢指针永远不会碰到快指针
    def MeetingNode(self, pHead):
        if pHead == None:
            return None
        pSlow = pHead.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
    def EntryNodeOfLoop(self, pHead):
        #相遇结点
        meetingNode = self.MeetingNode(pHead)
        if meetingNode == None:
            return None
        NodeLoop = 1
        flagNode = meetingNode

        #记录环一周的长度
        while flagNode.next != meetingNode:
            NodeLoop += 1
            flagNode = flagNode.next

        #
        pFast = pHead
        #快结点先走k个
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = pHead
        #快慢结点同时走n-k个会碰到一起，是环的初始结点
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

    def EntryNodeOfLoop(self, pHead):
        slow, fast = pHead, pHead
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


    # 使用断链法，在当前结点访问完毕后，断掉指向当前结点的指针。因此，最后一个被访问的结点一定是入口结点。
    def EntryNodeOfLoop(self, pHead):
        if pHead == None:
            return None
        while pHead.next:
            temp = pHead
            pHead = pHead.next

        return pHead
