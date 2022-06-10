""" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
A hash table solution which is the same as Two Sum II

Time complexity: O(n), note that `in` is O(1) for set and dictionary
"""
class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        d = {}
        for i in range(len(A)):
            if t-A[i] not in d:
                d[A[i]] = i
            else:
                return [d[t-A[i]]+1, i+1]