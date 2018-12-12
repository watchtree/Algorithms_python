#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/11/22 8:02
# software: PyCharm
# question: 扑克牌顺子
'''
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
'''
class Solution:

    #运行时间：25ms占用内存：5732k
    def IsContinuous(self, numbers):
        length = len(numbers)
        if length != 5:
            return False
        numbers.sort()
        countOnes = 0
        while(numbers[countOnes]==0):
            countOnes += 1
        startIndex = countOnes
        temp = numbers[startIndex]
        for i in range(startIndex+1, length):
            if numbers[i] - temp == 1:
                temp = temp + 1
            else:
                if numbers[i] -temp -1 <= countOnes and numbers[i] -temp -1 > 0:
                    countOnes = countOnes - (numbers[i] - temp - 1)
                    temp = numbers[i]
                else:
                    return False
        return True

    # 运行时间：28 ms占用内存：5752k
    def IsContinuous2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        numbers = sorted(numbers)
        numbersOfzero = 0
        numbersOfGap = 0

        #统计0 的数目
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numbersOfzero += 1
            i += 1
        # 统计间隔的数目
        small = numbersOfzero
        big = small + 1
        while big < len(numbers):
            #相当直接排除
            if numbers[small] == numbers[big]:
                return False
            numbersOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numbersOfGap > numbersOfzero else True


test2 = [0,3,1,6,4]
s = Solution()
print(s.IsContinuous(test2))
