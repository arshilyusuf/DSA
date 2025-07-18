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