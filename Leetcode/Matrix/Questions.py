from collections import *
from typing import *
# 59. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0]*n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        # res =[]
        number =1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                # res.append(number)
                grid[top][i]=number
                number+=1
            top += 1

            for i in range(top, bottom + 1):
                # res.append(number)
                grid[i][right]=number
                number+=1
            right -= 1

            if top <= bottom:

                for i in range(right, left - 1, -1):
                    # res.append(number)
                    grid[bottom][i]=number
                    number+=1
                bottom -= 1

            if left <= right:

                for i in range(bottom, top - 1, -1):
                    # res.append(number)
                    grid[i][left]=number
                    number+=1
                left += 1

        return grid