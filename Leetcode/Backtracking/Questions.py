from collections import *
from typing import *


# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }
        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return
            for letter in keypad[int(digits[index])]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, rem, path):
            if rem == 0:
                result.append(path)
                return
            for i in range(start, n + 1):
                backtrack(i + 1, rem - 1, path + [i])

        backtrack(1, k, [])
        return result


# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])
                # can also use set to track visited

        backtrack([], nums)
        return result


# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, sum, path):
            if sum > target:
                return
            if sum == target:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, sum + candidates[i], path)
                path.pop()

        backtrack(0, 0, [])
        return result


# 51. N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, down, up = set(), set(), set()
        result = []

        def backtrack(row, board):
            if row == n:
                result.append(board[:])
                return
            for j in range(n):
                if j not in cols and (row - j) not in down and (row + j) not in up:
                    row_str = "." * j + "Q" + "." * (n - j - 1)
                    cols.add(j)
                    down.add(row - j)
                    up.add(row + j)

                    backtrack(row + 1, board + [row_str])

                    cols.remove(j)
                    down.remove(row - j)
                    up.remove(row + j)

        backtrack(0, [])
        return result

# N QUEENS II
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, down, up = set(), set(), set()
        count = [0]

        def backtrack(row, board):
            if row == n:
                count[0] += 1
                return
            for j in range(n):
                if j not in cols and (row - j) not in down and (row + j) not in up:
                    row_str = "." * j + "Q" + "." * (n - j - 1)
                    cols.add(j)
                    down.add(row - j)
                    up.add(row + j)

                    backtrack(row + 1, board + [row_str])

                    cols.remove(j)
                    down.remove(row - j)
                    up.remove(row + j)

        backtrack(0, [])
        return count[0]


# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(start, close, path):
            if start == close == 0:
                result.append(path[:])
                return
            if start:
                newPath = path[:] + "("
                backtrack(start - 1, close, newPath)
            if close > start:
                newPath = path[:] + ")"
                backtrack(start, close - 1, newPath)

        backtrack(n, n, "")
        return result


# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"  # visited

            found = (
                backtrack(i + 1, j, index + 1)
                or backtrack(i - 1, j, index + 1)
                or backtrack(i, j + 1, index + 1)
                or backtrack(i, j - 1, index + 1)
            )

            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False