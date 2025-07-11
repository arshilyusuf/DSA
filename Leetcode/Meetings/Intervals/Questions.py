from collections import *
from typing import *
from heapq import *
# 2402. Meeting Rooms III
# You are given an integer n. There are n rooms numbered from 0 to n - 1.
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
# Meetings are allocated to rooms in the following manner:
# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
# A half-closed interval [a, b) is the interval between a and b including a and not including b
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        roomHeap = list(range(n))  
        heapify(roomHeap)
        
        heap = [] 
        freq = [0] * n
        
        for meeting in meetings:
            start, end = meeting
            
            while heap and heap[0][0] <= start:
                meetingEnd, room = heappop(heap)
                heappush(roomHeap, room)
            
            if roomHeap:
                room = heappop(roomHeap)
                heappush(heap, (end, room))
                
            else:
                meetingEnd, room = heappop(heap)
                duration = end - start
                heappush(heap, (meetingEnd + duration, room))
            freq[room] += 1
        
        maxRoom = 0
        maxTimes = 0
        for i in range(n):
            if freq[i] > maxTimes:
                maxTimes = freq[i]
                maxRoom = i
        
        return maxRoom