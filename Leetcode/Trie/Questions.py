# Implement Trie
# Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.
# 1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.
# 2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.
# 3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.
# 4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.
# 5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.
# Note:
# 1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.
# 2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.
# Can you help Ninja implement the "TRIE" data structure?
from collections import *
from typing  import *
class NodeNinja:
    def __init__(self):
        self.links = [None]*26
        self.ew = 0
        self.cp = 0
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch)-ord('a')]=node
    def get(self, ch):
        return self.links[ord(ch)-ord('a')]
    def increaseEnd(self):
        self.ew+=1
    def increaseCount(self):
        self.cp+=1
    def deleteEnd(self):
        self.ew-=1
    def deleteCount(self):
        self.cp-=1
    def getEnd(self):
        return self.ew
    def getPrefix(self):
        return self.cp
class TrieNinja:
    def __init__(self):
        self.root = self.NodeNinja()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], self.NodeNinja())
            node = node.get(word[i])
            node.increaseCount()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return 0
            node = node.get(word[i])
        return node.getEnd()

    def countWordsStartingWith(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return 0
            node = node.get(word[i])
        return node.getPrefix()
    def erase(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return
            node = node.get(word[i])
            node.deleteCount()
        node.deleteEnd()    

# Longest Valid Word with All Prefixes
# Given an array of strings words[], find the longest string such that every prefix of it is also present in words[]. If multiple strings have the same maximum length, return the lexicographically smallest one.

# If no such string is found, return an empty string.
class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] is not None
    def get(self, ch):
        return self.links[ord(ch)-ord('a')]
    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i], Node())
            node = node.get(word[i])
        node.setEnd()
    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.containsKey(word[i]):
                return False
            node = node.get(word[i])
        return node.isEnd()
    def checkIfPrefixExists(self, word):
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]):
                node = node.get(word[i])
                if node.isEnd()==False:
                    return False
            else: return False
        return True
    
        
class Solution:
    def longestValidWord(self, words):
        words.sort(reverse=True)
        longest = ""
        trie = Trie()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.checkIfPrefixExists(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word
        return longest if longest is not "" else "None"


# Count of distinct substrings
# Given a string of length N of lowercase alphabet characters. The task is to complete the function countDistinctSubstring(), which returns the count of total number of distinct substrings of this string.
# Input:
# The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case contains a string str.
# Output:
# For each test case in a new line, output will be an integer denoting count of total number of distinct substrings of this string.
# User Task:
# Since this is a functional problem you don't have to worry about input, you just have to complete the function countDistinctSubstring().

def countDistinctSubstring(s):
    ans = 0 
    root = Node()
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if not node.containsKey(s[j]):
                ans+=1
                node.put(s[j], Node())
            node = node.get(s[j])
    return ans 

# 421. Maximum XOR of Two Numbers in an Array
# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

class NodeXOR:
    def __init__(self):
        self.links = [None]*2
    def containsKey(self,key):
        return self.links[key] is not None
    def put(self,key, node):
        self.links[key] = node
    def get(self, key):
        return self.links[key]
class TrieXOR:
    def __init__(self):
        self.root = NodeXOR()
    def insert(self, key):
        node = self.root
        for i in range(31, -1, -1):
            bit = (key >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, NodeXOR())
            node = node.get(bit)
    def maxXor(self, num):
            node = self.root
            maxXor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggledBit = 1 - bit
                if node.containsKey(toggledBit):
                    maxXor |= (1 << i) 
                    node = node.get(toggledBit)
                else:
                    node = node.get(bit)
            return maxXor                 
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = TrieXOR()
        for num in nums:
            trie.insert(num)
        ans = 0
        for num in nums:
            ans = max(ans, trie.maxXor(num))
        return ans
    
    # def findMaximumXOR(self, nums: List[int]) -> int:
    #     maxXor = 0
    #     mask = 0
        
    #     for i in range(31, -1, -1):
    #         mask |= (1 << i)
    #         prefixes = {num & mask for num in nums}
    #         candidate = maxXor | (1 << i)
            
    #         for prefix in prefixes:
    #             if (candidate ^ prefix) in prefixes:
    #                 maxXor = candidate
    #                 break
                    
    #     return maxXor

# 1707. Maximum XOR With an Element From Array
# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            nums.sort()
            trie = TrieXOR()
            oQuery = [[query[1], query[0], idx] for idx, query in enumerate(queries)]
            oQuery.sort()
            ans = [-1]*len(queries)
            idx = 0 
            for query in oQuery:
                mi = query[0]
                xi = query[1]
                qId = query[2]

                while idx < len(nums) and nums[idx] <= mi:
                    trie.insert(nums[idx])
                    idx+=1
                if idx != 0 : 
                    ans[qId] = trie.maxXor(xi)
            return ans