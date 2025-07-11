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