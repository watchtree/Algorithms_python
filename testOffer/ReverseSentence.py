#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/21 10:31
# software: PyCharm
# question: 翻转单词顺序列
'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''
class Solution:
    # 运行时间：25ms占用内存：5724k
    def ReverseSentence(self, s):
        sList = s.split(" ")
        length = len(sList)
        if length <= 1:
            return s
        for i in range(length//2):
            sList[i], sList[length-1-i] = sList[length-1-i], sList[i]
        return " ".join(sList)
    #代码简化：运行时间：36ms占用内存：5728k
    def ReverseSentence2(self, s):
        sList = s.split(" ")
        return " ".join(sList[::-1])

    # V2.0
    '''
    首先需要写一个reverse函数，把任何输入的字符串完全翻转。
    然后从前往后依次遍历新字符串，如果遇到空格，就把空格前的字符串用reverse翻转，添加空格，继续遍历。
    需要注意的是，如果新字符串结尾不是空格，当遍历到结尾的时候，前一个空格到结尾的字符串没有翻转，
    因此记得跳出遍历后，需要再完成一次翻转操作。
    '''
    def Reverse(self, alist):
        if alist == None or len(alist) <= 0:
            return ''
        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist
    def ReverseSentence3(self, s):
        if s == None or len(s) <= 0:
            return ''
        strList = list(s)
        strList = self.Reverse(strList)
        pBegin = 0
        pEnd = 0
        resultStr = ''
        listTemp = []
        while pEnd < len(s):
            #指针达到最后一个字符，翻转最后一个单词，跳出循环
            if pEnd == len(s) - 1:
                listTemp.append(self.Reverse(strList[pBegin]))
                break
            #鉴定开头是否为空格
            if strList[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
                listTemp.append(' ')
            #当达到
            elif strList[pEnd] == ' ':
                listTemp.append(self.Reverse(strList[pBegin:pEnd]))
                pBegin = pEnd
            else:
                pEnd += 1
        for i in listTemp:
            resultStr += ''.join(i)
        return resultStr


s = "I am a student."
S = Solution()
print(S.ReverseSentence3(s))