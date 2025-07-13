from collections import *
from typing import *
# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        n, m = len(words), len(words[0])
        subLen = n * m
        stringMap = {}
        for word in words:
            stringMap[word] = stringMap.get(word, 0) + 1
        result = []
        for offset in range(m):
            i = j = offset
            copyMap = {}
            count = 0

            while j + m <= len(s):
                word = s[j:j + m]
                j += m

                if word in stringMap:
                    copyMap[word] = copyMap.get(word, 0) + 1
                    count += 1

                    while copyMap[word] > stringMap[word]:
                        left_word = s[i:i + m]
                        copyMap[left_word] -= 1
                        count -= 1
                        i += m

                    if count == n:
                        result.append(i)
                else:
                    copyMap.clear()
                    count = 0
                    i = j

        return result

# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        curWindow = defaultdict(int)

        for c in t:
            need[c] += 1

        i = 0
        count = 0
        minLen = float('inf')
        ans = ""

        for j in range(len(s)):
            c = s[j]
            if c in need:
                curWindow[c] += 1
                if curWindow[c] == need[c]:
                    count += 1

            while count == len(need):
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    ans = s[i:j+1]

                ch = s[i]
                if ch in need:
                    curWindow[ch] -= 1
                    if curWindow[ch] < need[ch]:
                        count -= 1
                i += 1

        return ans

# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules                
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        blocks = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    bit = int(board[i][j]) - 1
                    mask = 1 << bit
                    
                    if rows[i] & mask:
                        return False
                    rows[i] |= mask

                    if cols[j] & mask:  
                        return False
                    cols[j] |= mask

                    blockIdx = (i // 3) * 3 + (j // 3)  
                    if blocks[blockIdx] & mask:
                        return False
                    blocks[blockIdx] |= mask
        return True
