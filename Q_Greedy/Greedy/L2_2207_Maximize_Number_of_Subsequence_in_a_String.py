""" https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
Heuristics from lee: https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/discuss/1863900/JavaC%2B%2BPython-Straight-Forward-Solution
If we add pattern[0], the best option is to add at the begin.
If we add pattern[1], the best option is to add at the end.
"""


class Solution:
    def maximumSubsequenceCount(self, A, p):
        # Assume adding p[0] of pattern at starting
        ans1 = 0
        cnt = 1
        for i in range(len(A)):
            if A[i] == p[1]:
                ans1 += cnt
            if A[i] == p[0]:
                cnt += 1

        # Assume adding p[1] of pattern at starting
        ans2 = 0
        cnt = 1
        for i in reversed(range(len(A))):
            if A[i] == p[0]:
                ans2 += cnt
            if A[i] == p[1]:
                cnt += 1
        return max(ans1, ans2)
