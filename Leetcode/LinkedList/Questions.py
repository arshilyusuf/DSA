from collections import *
from typing import *
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interleave copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list
        dummy = Node(0)
        copy = dummy
        curr = head

        while curr:
            copy.next = curr.next
            curr = curr.next.next  # Restore original
            copy = copy.next

        return dummy.next

# 138. Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interleave copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list
        dummy = Node(0)
        copy = dummy
        curr = head

        while curr:
            copy.next = curr.next
            curr = curr.next.next  # Restore original
            copy = copy.next

        return dummy.next

# 86. Partition List
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        leastPointer = dummy  # Last node < x
        prev = dummy
        curr = head

        while curr:
            if curr.val < x:
                if leastPointer.next == curr:
                    # Already in correct place
                    leastPointer = curr
                    prev = curr
                    curr = curr.next
                else:
                    # Remove curr
                    prev.next = curr.next
                    # insertFront after leastPointer
                    curr.next = leastPointer.next
                    leastPointer.next = curr
                    leastPointer = curr
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next

# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity
class Node:
    def __init__(self, key=0, val=0, right=None, left=None):
        self.key = key
        self.val = val
        self.right = right
        self.left = left

class LRUCache:

    def __init__(self, capacity: int):
        self.lruMap = {}  
        self.capacity = capacity
        self.currCapacity = 0

        self.root = Node()  # Head (MRU)
        self.tail = Node()  # Tail (LRU)
        self.root.right = self.tail
        self.tail.left = self.root

        self.mru = self.root 
        self.lru = self.tail

    def remove(self, node):
        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev

    def insertFront(self, node):
        node.right = self.root.right
        node.left = self.root
        self.root.right.left = node
        self.root.right = node

    def get(self, key: int) -> int:
        if key not in self.lruMap:
            return -1
        node = self.lruMap[key]
        self.remove(node)
        self.insertFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lruMap:
            node = self.lruMap[key]
            node.val = value
            self.remove(node)
            self.insertFront(node)
        else:
            if self.currCapacity == self.capacity:
                # Remove least recently used node
                lru_node = self.tail.left
                self.remove(lru_node)
                del self.lruMap[lru_node.key]
                self.currCapacity -= 1

            newNode = Node(key, value)
            self.lruMap[key] = newNode
            self.insertFront(newNode)
            self.currCapacity += 1
