""" https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""
class Solution:
    def checkIfPangram(self, A: str) -> bool:
        return len(set(A))==26