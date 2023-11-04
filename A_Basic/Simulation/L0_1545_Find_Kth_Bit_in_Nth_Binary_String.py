""" https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
simulate string formation process
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for _ in range(n):
            s = s + '1' + ''.join(['1' if c=='0' else '0' for c in s][::-1])
        return s[k-1]