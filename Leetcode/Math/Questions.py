
from collections import *
from typing import *
# 60. Permutation Sequence
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = [i for i in range(1, n+1)]
        
        for i in range(1, n):
            fact *= i
        
        ans = ""
        k -= 1  
        while numbers:
            index = k // fact
            ans += str(numbers[index])
            numbers.pop(index)
            
            if not numbers:
                break
            
            k %= fact
            fact //= len(numbers)

        return ans

# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

class Solution:
    def divide(self, dvd: int, dvs: int) -> int:
        if dvd == dvs:
            return 1

        sign = (dvd >= 0) == (dvs >= 0)

        dividend = abs(dvd)
        divisor = abs(dvs)
        ans = 0

        while dividend >= divisor:
            c = 0
            while dividend >= (divisor << (c + 1)):
                c += 1
            ans += 1 << c
            dividend -= divisor << c

        if not sign:
            ans = -ans

        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        return min(max(ans, INT_MIN), INT_MAX)