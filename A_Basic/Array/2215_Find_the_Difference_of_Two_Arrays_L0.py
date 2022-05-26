""" https://leetcode.com/problems/find-the-difference-of-two-arrays/
find difference set of A and B
"""
class Solution:
    def findDifference(self, A: List[int], B: List[int]) -> List[List[int]]:
        A, B = set(A), set(B)
        return [A-B, B-A]