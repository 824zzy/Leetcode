""" https://leetcode.com/problems/find-all-duplicates-in-an-array/
negative encoding, note that ans doesn't count as extra space
"""


class Solution:
    def findDuplicates(self, A: List[int]) -> List[int]:
        ans = []
        for x in A:
            if A[abs(x) - 1] < 0:
                ans.append(abs(x))
            A[abs(x) - 1] *= -1
        return ans
