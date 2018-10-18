#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/18 7:01
# software: PyCharm
# question: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
#
class ListNode:
    #设定默认构造x=None空节点
    def __init__(self, x = None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        #当空集时返回None或者是[]
        # if listNode.val == None:
        #     return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l




if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    singleNode = ListNode(12)

    test = ListNode()

    S = Solution()
    print(S.printListFromTailToHead(node1))
    print(S.printListFromTailToHead(test))
    print(S.printListFromTailToHead(singleNode))
