""" https://leetcode.com/problems/increasing-triplet-subsequence/submissions/
maintain an increasing list by bisect_left
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