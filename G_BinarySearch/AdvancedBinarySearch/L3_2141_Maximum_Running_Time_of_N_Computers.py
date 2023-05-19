""" https://leetcode.com/problems/maximum-running-time-of-n-computers/
God DBa: https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1693174/Python-short-binary-search-explained

Let us look at the n biggest batteries.

We can deal with the rest of battaries as with one big battery, call it small.
What we need to do now is binary search: ask question: given m, can we survive m time. For each batery which is >=m, we are OK. For smaller battaries we need to use our small.
"""
class Solution:
    def maxRunTime(self, n, B):
        def fn(m):
            cnt = 0
            for x in B[:n]:
                cnt += max(m-x, 0)
            return cnt>small
        
        B = sorted(B, reverse=True)
        small = sum(B[n:])
        l, r = 0, sum(B) + 1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l-1