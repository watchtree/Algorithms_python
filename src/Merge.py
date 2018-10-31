#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/31 20:51
# software: PyCharm
# question: 合并两个排序的链表
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    # 递归方法
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead

    #非递归方法
    def Merge2(self, pHead1, pHead2):
        #初始判定，设定合成链表起始node
        if pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                pMergeHead = pHead1
                pHead1 = pHead1.next
            else:
                pMergeHead = pHead2
                pHead2 = pHead2.next
        elif pHead1:
            return pHead1
        else:
            return pHead2
        #进行合成，依次进行排序连接
        cur = pMergeHead
        while(pHead1 and pHead2):
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        #检查各个链表是否还存在剩余

        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2

        return pMergeHead

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    S = Solution()
    new = S.Merge2(node1, node4)
    print(new.val)