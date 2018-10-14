#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wttree
# datetime:2018/10/13 19:20
# software: PyCharm

# question：输入一个矩阵(不一定是标准的n*n)，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

class Solution:

    #v1.0分为两个部分函数完成，一是PrintMatrixInCircle打印矩阵某一圈的数字，
    def printMatrix(self, matrix):
        newmat = []
        if matrix == None:
            return None
        rows = len(matrix) #矩阵行数
        columns = len(matrix[0]) #矩阵列数
        start = 0
        while rows > start * 2 and columns > start * 2:
            mat = self.PrintMatrixInCircle(matrix, columns, rows, start)
            newmat.extend(mat)
            start += 1
        return newmat

    def PrintMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 -start
        mat = []
        for i in range(start, endX + 1):
            number = matrix[start][i]
            mat.append(number)
            #包含end=''作为print()BIF的一个参数，会使该函数关闭“在输出中自动包含换行”的默认行为。其原理是：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。这个只有Python3有用，Python2不支持

        if start < endY: #在矩阵大小为奇数项时， 最后一次只输出其中心值
            for i in range(start + 1, endY + 1):
                number = matrix[i][endX]
                mat.append(number)

        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endY][i]
                mat.append(number)
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                mat.append(number)
        return mat

        #v2.0组合单个函数版本
    def printMatrix2(self, matrix):
        newmat = []
        if matrix == None:
            return None
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > start*2 and columns > start*2:
            endX = columns - 1 - start
            endY = rows - 1 - start
            mat = []
            for i in range(start, endX + 1):
                number = matrix[start][i]
                mat.append(number)

            if start < endY:
                for i in range(start + 1, endY + 1):
                    number = matrix[i][endX]
                    mat.append(number)\

            if start < endX and start < endY:
                for i in range(endX - 1, start - 1, -1):
                    number = matrix[endY][i]
                    mat.append(number)

            if start < endX and start < endY - 1:
                for i in range(endY - 1, start, -1):
                    number = matrix[i][start]
                    mat.append(number)
            newmat.extend(mat)
            start += 1
        return newmat

    #模仿魔方逆时针旋转，输出并删除一行后，进行一次逆时针旋转，重复多次
    def printMatrix3(self, matrix):
        result = []
        while(matrix):
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self, matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat

    #单个函数实现魔方翻转打印
    def printMatrix4(self, matrix):
        result = []
        while(matrix):
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            num_r = len(matrix)
            num_c = len(matrix[0])
            newmat = []
            for i in range(num_c):
                newmat2 = []
                for j in range(num_r):
                    newmat2.append(matrix[j][i])
                newmat.append(newmat2)
            newmat.reverse()#反向列表中的元素
            matrix = newmat
        return result

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
out = S.printMatrix4(matrix)
print(out)
print('\n')
out = S.printMatrix4(matrix2)
print(out)
print('\n')
out = S.printMatrix4(matrix3)
print(out)
