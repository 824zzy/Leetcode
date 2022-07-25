""" https://leetcode.com/problems/longest-well-performing-interval/submissions/
962 and 1124 are similar to each other.

prefix sum + farmost greater monotonic stack
"""
class Solution:
    def longestWPI(self, A: List[int]) -> int:
        A = [1 if x>8 else -1 for x in A]
        prefix = list(accumulate(A, initial=0))
        
        stk = []
        for i in range(len(prefix)):
            if not stk or prefix[stk[-1]]>prefix[i]:
                stk.append(i)
        
        ans = 0
        for i in reversed(range(len(prefix))):
            while stk and prefix[stk[-1]]<prefix[i]:
                ans = max(ans, i-stk.pop())
        return ans