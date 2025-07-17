from collections import *
from typing import *

def constructSeg(seg, index, arr, l, r):
    if l==r:
        seg[index]=arr[l]
        return arr[l]
    mid = (l+r)//2
    seg[index] = constructSeg(seg, 2*index+1, arr, l, mid) + constructSeg(seg, 2*index+2, arr, mid+1, r)
    return seg[index]

def getSum(seg, index, sl, sr, l, r):
    if l<=sl and r>=sr:
        return seg[index]
    if sr < l or sl > r:
        return 0
    mid = (sl + sr)//2
    return getSum(2*index+1, sl, mid, l, r)+getSum(2*index+1, mid+1, sr, l, r)

def update(seg, index, sl, sr, pos, diff):
    if pos < sl or pos > sr:
        return
    seg[index] += diff
    if sl != sr:
        mid = (sl + sr) // 2
        update(seg, 2 * index + 1, sl, mid, pos, diff)
        update(seg, 2 * index + 2, mid + 1, sr, pos, diff)