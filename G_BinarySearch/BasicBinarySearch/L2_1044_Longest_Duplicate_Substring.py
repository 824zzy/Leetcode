""" https://leetcode.com/problems/longest-duplicate-substring/
The same as L1_1062_Longest_Repeating_Substring.py
"""
class Solution:
    def longestDupSubstring(self, A: str) -> str:
        A += '*'
        self.ans = ''

        def fn(x):
            seen = set()
            w = A[:x]
            seen.add(w)
            for i in range(x, len(A)):
                w = w[1:]+A[i]
                if w in seen:
                    self.ans = max(self.ans, w, key=len)
                    return False
                seen.add(w)
            return True

        l, r = 1, len(A)
        while l<r:
            m = (l+r)//2
            x = fn(m)
            if x:
                r = m
            else:
                l = m+1
        return ''.join(self.ans)