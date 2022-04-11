""" https://leetcode.com/problems/count-binary-substrings/
since we only need to count substrings that grouped consecutively,
1. use groupby to find length of consecutive 1's and 0's
2. find valid substrings by min(A[i], A[i+1])
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        A = [len(list(v)) for k, v in groupby(s)]
        ans = 0
        for i in range(len(A)-1):
            ans += min(A[i], A[i+1])
        return ans