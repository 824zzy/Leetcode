""" https://leetcode.com/problems/increasing-triplet-subsequence/submissions/
the same as: 300.
1. find longest increasing subsequence by maintain an increasing list by bisect_left
2. check the length of LIC if larger or equal than 3
"""
class Solution:
    def increasingTriplet(self, A: List[int]) -> bool:
        ans = []
        for x in A:
            if not ans or ans[-1]<x: ans.append(x)
            else:
                i = bisect_left(ans, x)
                ans[i] = x
        return len(ans)>=3