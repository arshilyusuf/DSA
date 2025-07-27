from collections import *
from typing import *
import bisect
# 2080. Range Frequency Queries
# Design a data structure to find the frequency of a given value in a given subarray.
# The frequency of a value in a subarray is the number of occurrences of that value in the subarray.
# Implement the RangeFreqQuery class:
# RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
# int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
# A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive)
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.mp = defaultdict(List)
        for i in range(len(arr)):
            self.mp[arr[i]].append(i)
        
        
    def query(self, left: int, right: int, value: int) -> int:
        rightIndex = bisect.bisect_right(self.mp[value], right) 
        leftIndex = bisect.bisect_left(self.mp[value], left) 
        return rightIndex-leftIndex
        
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total //2
        if m < n:
            a, b = b, a 
            n, m = m, n
        l, r = 0 , n-1
        while True:
            midA = (l+r) // 2
            midB = half - midA -2

            aLeft, aRight = a[midA] if midA>=0 else float('-inf'), a[midA+1] if midA + 1 < n else float('inf')
            bLeft, bRight = b[midB] if midB>=0 else float('-inf'), b[midB+1] if midB + 1 < m else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                #odd
                if total %2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight))/2
            elif aLeft > bRight:
                r = midA -1
            else:
                l = midA + 1