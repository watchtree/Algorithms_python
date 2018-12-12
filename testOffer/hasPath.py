#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/12/10 9:10
# software: PyCharm
# question: 矩阵中的路径
'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
'''
回溯法。任选一个格子作为路径的起点。
假设矩阵中某个格子的字符为ch并且这个格子将对应于路径上的第i个字符。
如果路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。
如果路径上的第i个字符正好是ch，那么往相邻的格子寻找路径上的第i+1个字符
除在矩阵边界上的格子外，其他各自都有4个相邻的格子
重复这个过程直到路径上的所有字符都在矩阵中找到相应的位置。
'''
class Solution:
    #运行时间：40ms占用内存：5860k
    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [0]*(rows*cols)#判定路上上是否走过
        pathLength = 0
        #将每一个格子的左边输出，如果存在一个判定成里，则返回True
        for row in range(rows):
            for col in range(cols):
                #递归方式判定
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        #利用递归的方法，一个一个判定路径上是否符合要求
        if len(path) == pathLength:
            #当路径可以走到最后一个时，说明前面的均符合要求，返回
            return True
        hasPath = False
        #如果当前输入起点位置符合要求且
        #从矩阵中定位到第几个数字row行数 * cols + col对应路径里的数字相等
        if row >= 0 and row < rows and col >= 0 and col < cols and \
            matrix[row * cols + col] == path[pathLength] and not visited[row*cols + col]:
            pathLength += 1
            visited[row*cols + col] = True#走过的距今设定为True
            #上下左右四个方向，上面所以需要提前判断方向
            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)
            if not hasPath:
                #如果这个各自不符合要要求，需要先返回上一步，并且这个格子当没走过，进行下一步寻找方向
                pathLength -= 1
                visited[row*cols+col] = False
        return hasPath