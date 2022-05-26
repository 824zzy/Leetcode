""" https://leetcode.com/problems/decode-the-slanted-ciphertext/
simulation
"""
class Solution:
    def decodeCiphertext(self, T: str, rows: int) -> str:
        ans = []
        cols = len(T)//rows
        for j in range(cols):
            i = 0
            while i*cols+j<len(T):
                ans.append(T[i*cols+j])
                i, j = i+1, j+1
        return ''.join(ans).rstrip()