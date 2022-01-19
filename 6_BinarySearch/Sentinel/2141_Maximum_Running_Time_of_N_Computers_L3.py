""" https://leetcode.com/problems/maximum-running-time-of-n-computers/
God DBa: https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1693174/Python-short-binary-search-explained

Let us look at the n biggest batteries.

We can deal with the rest of battaries as with one big battery, call it accumulator.
What we need to do now is binary search: ask question: given x, can we survive x time. For each batery which is >= x, we are OK. For smaller battaries we need to use our accumulator.
"""
class Solution:
    def maxRunTime(self, n, B):
        B = sorted(B)[::-1]
        small = sum(B[n:])

        l, r = 0, sum(B) + 1
        while l<r:
            m = (l+r)//2
            to_do = sum(max(m - x, 0) for x in B[:n])
            if to_do > small: r = m
            else: l = m+1
     
        return l-1