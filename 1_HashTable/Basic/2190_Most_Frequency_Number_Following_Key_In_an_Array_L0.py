""" https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/
Use counter to compute target's frequencies, then return the most frequent one
"""
class Solution:
    def mostFrequent(self, A: List[int], key: int) -> int:
        cnt = Counter()
        for i, x in enumerate(A):
            if i+1<len(A) and A[i]==key: cnt[A[i+1]] += 1
        return max(cnt.keys(), key=lambda x: cnt[x])