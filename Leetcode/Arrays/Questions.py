from collections import *
from typing import *

# 718. Maximum Length of Repeated Subarray
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays4
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1), len(nums2)
        maxLen=0
        # def dp(i, j):
        #     if not (i < m and j < n):
        #         return 0
        #     equal, notequal = 0,0
        #     if nums1[i] == nums2[j]:
        #         equal = 1 + dp(i+1,j+1)
        #     else:
        #         notequal = max(dp(i, j+1),dp(i+1, j))
        #     return max(equal, notequal)
        
        # return dp(0,0)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    maxLen = max(maxLen, dp[i][j])
        return maxLen