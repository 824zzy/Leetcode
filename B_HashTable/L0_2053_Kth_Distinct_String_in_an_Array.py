""" https://leetcode.com/problems/kth-distinct-string-in-an-array/
find kth distinct string by counter
"""
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for x in arr: 
            if freq[x] == 1: k -= 1
            if k == 0: return x
        return ""