from collections import *
from typing import * 

# 199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size - 1:
                    result.append(node.val)

        return result
    
# 2385. Amount of Time for Binary Tree to Be Infected
# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        visited = set([start])

        def buildAdj(node):
            # if not node:
            #     return
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                buildAdj(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                buildAdj(node.right)

        buildAdj(root)
        q = deque([start])
        visited.add(start)
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                
                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            ans+=1
        return ans-1