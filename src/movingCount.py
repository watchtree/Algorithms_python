#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/11 7:44
# software: PyCharm
# question: 机器人的运动范围
'''
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
'''
'''
回溯法。类似于面试题66。把方格看成一个m*n的矩阵，从（0，0）开始移动。
当准备进入坐标(i, j)是，通过检查坐标的数位来判断机器人能否进入。如果能进入的话，接着判断四个相邻的格子。
'''
#运行时间：32ms占用内存：5728k
class Solution:
    def movingCount(self, threshold, rows, cols):
        visited = [False] * (rows*cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        return count

    #运动格统计
    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited) + \
                        self.movingCountCore(threshold, rows, cols, row+1, col, visited) + \
                        self.movingCountCore(threshold, rows, cols, row, col-1, visited) + \
                        self.movingCountCore(threshold, rows, cols, row, col+1, visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if row >= 0 and row < rows and col >= 0 and col <cols and \
            self.getDightSum(row) + self.getDightSum(col)<= threshold and \
            not visited[row*cols + col]:
            return True
        return False

    #统计数字的位数相加
    def getDightSum(self, number):
        sum = 0
        while number > 0:
            sum += (number%10)
            number = number // 10
        return sum