from collections import * 
from typing import * 

# 307. Range Sum Query - Mutable
# Given an integer array nums, handle multiple queries of the following types:
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]  
        self.seg = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _build(self, index: int, l: int, r: int) -> int:
        if l == r:
            self.seg[index] = self.nums[l]
            return self.seg[index]
        mid = (l + r) // 2
        left = self._build(2 * index + 1, l, mid)
        right = self._build(2 * index + 2, mid + 1, r)
        self.seg[index] = left + right
        return self.seg[index]

    def _update(self, index: int, sl: int, sr: int, pos: int, diff: int):
        if pos < sl or pos > sr:
            return
        self.seg[index] += diff
        if sl != sr:
            mid = (sl + sr) // 2
            self._update(2 * index + 1, sl, mid, pos, diff)
            self._update(2 * index + 2, mid + 1, sr, pos, diff)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update(0, 0, self.n - 1, index, diff)

    def getSum(self, index: int, sl: int, sr: int, l: int, r: int) -> int:
        if l <= sl and r >= sr:
            return self.seg[index]
        if sr < l or sl > r:
            return 0
        mid = (sl + sr) // 2
        return self.getSum(2 * index + 1, sl, mid, l, r) + \
               self.getSum(2 * index + 2, mid + 1, sr, l, r)

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(0, 0, self.n - 1, left, right)
