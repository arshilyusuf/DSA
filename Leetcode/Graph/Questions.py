from collections import *
from typing import *

class Solution:
# Number of Islands
# Given an m x m 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        m, n = len(grid), len(grid[0])
        visited =[[False]*n for _ in range(m)]
        def isInBounds(i,j, m, n):
            return i>=0 and i<m and j>=0 and j<n
        def bfs(i,j):
            if isInBounds(i,j, m, n) and not visited[i][j] and grid[i][j]=="1":
                visited[i][j]=True
                bfs(i+1,j)
                bfs(i,j+1)
                bfs(i-1,j)
                bfs(i,j-1)
            return 
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=="1":
                    islands+=1
                    bfs(i,j)
        return islands
    
# 130. Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]

        def isInBounds(i,j, m, n):
            return i>=0 and i<m and j>=0 and j<n
        
        def dfs(i,j):
            if isInBounds(i,j,m,n) and not visited[i][j] and board[i][j]=='O':
                visited[i][j]=True
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
            
        for j in range(n):
            if board[0][j]=='O' and not visited[0][j]:
                dfs(0,j)
            if board[m-1][j]=='O' and not visited[m-1][j]:
                dfs(m-1,j)
        for i in range(m):
            if board[i][0]=='O' and not visited[i][0]:
                dfs(i,0)
            if board[i][n-1]=='O' and not visited[i][n-1]:
                dfs(i,n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and not visited[i][j]:
                    board[i][j]='X'
# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
# Definition for a Node.
    class Node:
        def __init__(self, val = 0, neighbors = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}
        
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            
            copy = self.Node(curr.val)
            cloned[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)    
# 399. Evaluate Division
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1.0
            if src == dest:
                return 1.0

            visited = set()
            queue = deque([(src, 1.0)])

            while queue:
                node, weight = queue.popleft()
                if node == dest:
                    return weight
                visited.add(node)

                for neighbor, val in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, weight * val))

            return -1.0

        return [bfs(src, dest) for src, dest in queries]
    
# Course Schedule
# total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n)]
        for src, dest in prerequisites:
            adj[src].append(dest)
        def kahns(adj):
            inDeg = [0]*n
            for list in adj:
                for i in list:
                    inDeg[i]+=1
            queue = deque()
            count = 0
            for i in range(n):
                if inDeg[i]==0:
                    queue.append(i)
                    count+=1
                    
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    inDeg[neighbor]-=1
                    if inDeg[neighbor]==0:
                        queue.append(neighbor)
                        count+=1
                        
            return (count == n) #if count is not the same as the number of vertices then there is a cycle in the graph, we detec this by topo sort

        return kahns(adj)
# Course Schedule II
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = [[] for _ in range(n)]
        for src, dest in prerequisites:
            adj[src].append(dest)
        def kahns(adj):
            order = []
            inDeg = [0]*n
            for list in adj:
                for i in list:
                    inDeg[i]+=1
            queue = deque()
            count = 0
            for i in range(n):
                if inDeg[i]==0:
                    queue.append(i)
                    order.append(i)
                    
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    inDeg[neighbor]-=1
                    if inDeg[neighbor]==0:
                        queue.append(neighbor)
                        order.append(neighbor)
            if len(order) != n:
                return []
    
            return order #if count is not the same as the number of vertices then there is a cycle in the graph, we detec this by topo sort

        return kahns(adj)
# 909. Snakes and Ladders
# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
# You start on square 1 of the board. In each move, starting from square curr, do the following:
# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.
# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def numberToCoordinates(i):
            row = (n - 1) - (i - 1) // n
            col = (i - 1) % n if ((n - row) % 2 == 1) else (n - 1 - (i - 1) % n)
            return row, col

        visited = set()
        q = deque()
        q.append((1, 0))  
        visited.add(1)

        while q:
            cell, steps = q.popleft()
            if cell == n * n:
                return steps
            for move in range(1, 7):
                nextCell = cell + move
                if nextCell > n * n:
                    continue
                i, j = numberToCoordinates(nextCell)
                if board[i][j] != -1:
                    nextCell = board[i][j]
                if nextCell not in visited:
                    visited.add(nextCell)
                    q.append((nextCell, steps + 1))

        return -1
# 433. Minimum Genetic Mutation
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        visited = set()
        queue.append((startGene, 0))
        visited.add(startGene)
        while queue:
            gene, mutations = queue.popleft()
            visited.add(gene)
            if gene == endGene:
                return mutations
            for i in range(len(gene)):
                ch = ['A', 'G', 'C', 'T']
                for c in ch:
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene not in visited and newGene in bank:
                        queue.append((newGene, mutations+1))
        return -1
    
# 127. Word Ladder
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord, 1))
        visited, wordList = set(), set(wordList)
        if endWord not in wordList:
            return 0
        visited.add(beginWord)
        while q:
            word, seq = q.popleft()
            visited.add(word)
            
            for i in range(len(word)):
                for idx in range(26):
                    letter = chr(idx + ord('a'))
                    if letter == word[i]:
                        continue
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord == endWord:
                        return seq+1
                    if newWord not in visited and newWord in wordList:
                        q.append((newWord, seq+1))
                        wordList.remove(newWord)
        return 0