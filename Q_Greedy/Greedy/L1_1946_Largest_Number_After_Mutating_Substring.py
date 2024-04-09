""" https://leetcode.com/problems/largest-number-after-mutating-substring/
once we find any change[c] larger than c, we can set the flag to True so that when we find a change[c]<c, we can immediately stop.
"""


class Solution:
    def maximumNumber(self, A: str, change: List[int]) -> str:
        ans = list(A)
        f = False
        for i, c in enumerate(A):
            c = int(c)
            if change[c] > c:
                ans[i] = str(change[c])
                f = True
            elif change[c] < c and f:
                break
        return ''.join(ans)
