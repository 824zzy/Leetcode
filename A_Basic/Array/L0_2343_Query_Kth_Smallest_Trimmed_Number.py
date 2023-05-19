""" https://leetcode.com/problems/query-kth-smallest-trimmed-number/
since the data size is small, so there is no tricks, just simulate rules

Time comlexity: (m*n*n) ~= 100*100*100 = 10^6
"""
class Solution:
    def smallestTrimmedNumbers(self, A: List[str], Q: List[List[int]]) -> List[int]:
        ans = []
        for n, i in Q:
            _A = sorted([(int(s[-i:]), idx) for idx, s in enumerate(A)])
            ans.append(_A[n-1][1])
        return ans