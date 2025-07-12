from collections import *
from typing import *
# 68. Text Justification
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.   
# THIS IS AN O(N^2) SOLN AS THE CONSTRAINTS ARE LOW
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        currStr = words[0]
        for word in words[1:]:
            if len(currStr) + 1 + len(word) <= maxWidth:
                currStr += " " + word
            else:
                result.append(currStr)
                currStr = word
        result.append(currStr)  

        for idx, sent in enumerate(result[:-1]):  
            wordCount = len(sent.split())
            
            if wordCount == 1:
                result[idx] = sent + " " * (maxWidth - len(sent))
                continue

            gaps = wordCount - 1
            extraSpace = maxWidth - len(sent)
            modul = extraSpace % gaps if gaps else 0
            needed = extraSpace // gaps if gaps else 0

            i = 0
            while i < len(sent) and gaps:
                if sent[i] != " ":
                    i += 1
                    continue
                sent = (
                    sent[:i+1]
                    + (" " * needed)
                    + (" " if modul > 0 else "")
                    + sent[i+1:]
                )
                if modul > 0:
                    modul -= 1
                while i < len(sent) and sent[i] == " ":
                    i += 1
                gaps -= 1

            result[idx] = sent
        result[-1] = result[-1] + " " * (maxWidth - len(result[-1]))
        return result
