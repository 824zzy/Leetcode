""" https://leetcode.com/problems/lexicographically-smallest-beautiful-string/
learn from lingshen: https://www.bilibili.com/video/BV1QX4y1m71X/?spm_id_from=333.337.search-card.all.click&vd_source=349088063a324f397a5e80a33effd4f0
"""
from header import *

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        A = [ord(c)-ord('a') for c in s]
        i = len(A)-1
        A[i] += 1
        while 0<=i<len(A):
            if A[i]==k:
                if i==0:
                    return ""
                A[i] = 0
                i -= 1
                A[i] += 1
            elif i and A[i]==A[i-1] or i>1 and A[i]==A[i-2]:
                A[i] += 1
            else:
                i += 1
        return ''.join(chr(ord('a')+a) for a in A)
            

""" cef
"abcz"
26
"dc"
4
"ced"
6

"abda"
"""