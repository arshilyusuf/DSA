from collections import *
from typing import *

def RabinKarpSearch(text:str, pattern:str, q:int)->List[int]:
    if not text or not pattern:
        return []
    d, n, m , p, t, h, result = 256, len(text), len(pattern), 0, 0, 1, []

    for i in range(m-1):
        h = (h*d) % q

    for i in range(m):
        p = (p*d + ord(pattern[i])) % q
        t = (t*d + ord(text[i])) % q

    for i in range(n-m+1):
        if p == t:
            if text[i:i+M] == pattern:
                result.append(i)
        if i < n -m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t += q
    return result

def KMPSearch(text: str, pattern: str) -> List[int]:
    if not text or not pattern:
        return []
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    def computeLPSArray(pattern: str, m: int, lps: List[int]) -> None:
        length = 0
        lps[0] = 0  
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
    computeLPSArray(pattern, m, lps)
    i = 0  
    result = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def BoyerMooreSearch(text: str, pattern: str) -> List[int]:
    if not text or not pattern:
        return []

    n, m = len(text), len(pattern)
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    result = []
    s = 0  # shift of the pattern with respect to text
    while s <= n - m:
        j = m - 1  # index of the last character in the pattern
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            result.append(s)

            s += (s + m < n) and (m - bad_char.get(text[s + m], -1)) or 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return result
