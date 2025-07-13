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
