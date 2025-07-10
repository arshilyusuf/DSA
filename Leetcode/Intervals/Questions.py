from collections import *
from typing import *
# 228. Summary Range
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result

# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for start, end in intervals:
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result

# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for start, end in intervals:
            if result and newInterval[0] <= end and newInterval[1] >= start:
                result[-1][1]=max(result[-1][1], newInterval[1])
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result

# 452. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for start, curEnd in points[1:]:
            if start > end:
                arrows += 1
                end = curEnd
        return arrows
