from collections import * 
from typing import *
# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n]=True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                size = len(word)
                if i+size <= n and s[i:i+size] == word:
                    dp[i]= dp[i+size]
                if dp[i]:
                    break
        return dp[0]
    
# 3196. Maximize Total Cost of Alternating Subarrays
# You are given an integer array nums with length n.
# The cost of a subarray nums[l..r], where 0 <= l <= r < n, is defined as:
# cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)r − l
# Your task is to split nums into subarrays such that the total cost of the subarrays is maximized, ensuring each element belongs to exactly one subarray.
# Formally, if nums is split into k subarrays, where k > 1, at indices i1, i2, ..., ik − 1, where 0 <= i1 < i2 < ... < ik - 1 < n - 1, then the total cost will be:
# cost(0, i1) + cost(i1 + 1, i2) + ... + cost(ik − 1 + 1, n − 1)
# Return an integer denoting the maximum total cost of the subarrays after splitting the array optimally.
# Note: If nums is not split into subarrays, i.e. k = 1, the total cost is simply cost(0, n - 1).
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        # def dfs(index, sign):
        #     if index >= n:
        #         return 0
            
        #     split = nums[index] + dfs(index+1, -1)
        #     dontsplit = nums[index]*sign + dfs(index+1, sign*(-1))

        #     return max(split, dontsplit)
        # return dfs(0,1)
        dp = [[0]*2 for _ in range(n+1)]
        for i in range(n-1, -1,-1):
            for j in range(2):
                sign = 1 if j==0 else -1
                split = nums[i] + dp[i+1][1]
                notsplit = nums[i]*sign + dp[i+1][j^1]
                dp[i][j] = max(split, notsplit)
        return dp[0][0]

# 673. Number of Longest Increasing Subsequence
# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}  
        lenLIS, res = 0, 0  

        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1  

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]  
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]

        return res

# Paint N Houses
# There is a row of N houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. Find the minimum cost to paint all houses.

# The cost of painting each house in red, blue or green colour is given in the array r[], g[] and b[] respectively.
class Solution:
    def distinctColoring (self, N, r, g, b):
        
        # def solve(i, prev_color):
        #     if i == N:
        #         return 0

        #     min_cost = float('inf')
        #     for color in range(3):
        #         if color == prev_color:
        #             continue
        #         if color == 0:
        #             cost = r[i]
        #         elif color == 1:
        #             cost = g[i]
        #         else:
        #             cost = b[i]
        #         min_cost = min(min_cost, cost + solve(i + 1, color))
        #     return min_cost

        # return solve(0, -1)
        
        dp = [[0]*3 for _ in range(N)]
        dp[0][0] = r[0]
        dp[0][1] = g[1]
        dp[0][2] = b[2]
        
        for i in range(N):
            dp[i][0] = r[i] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = g[i] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = b[i] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[N-1])