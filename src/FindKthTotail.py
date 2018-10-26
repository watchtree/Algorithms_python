#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/26 7:08
# software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #v1.0 AC33% 在线编译未通过
    def FindKthToTail(self, head, k):
        temp = []
        count = 0
        while(head != None):
            temp.append(head)
            head = head.next
        if k>len(temp) or k<1:
            return
        return temp[count-k]

    #2.0
    '''
    这道题的思路很好
    如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
    第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
    然后两个指针一起遍历
    当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
    推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
    '''
    def FindKthTotail2(self, head, k):
        if head == None or k<=0:
            return None
        pAHead = head
        pBehead = None

        #第一个指针先往前走k-1步
        for i in range(k-1):
            if pAHead.next != None:
                pAHead = pAHead.next
            else:
                return None

        pBehead = head
        while(pAHead.next != None):#从第k个结点开始，两个指针一起遍历
            pAHead = pAHead.next #A会移动指导链表完结
            pBehead = pBehead.next #B移动n-k次正好指向倒数第四个结点

        return pBehead


node1 = ListNode(10)
node2 = ListNode('{}')
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.FindKthToTail(node1, 2).val)