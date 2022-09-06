""" https://leetcode.com/problems/subarray-sum-equals-k/
prefix sum + two sum
"""
class Solution:
    def subarraySum(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        ans = 0
        cnt = Counter()
        
        for x in A:
            ans += cnt[x-k]
            cnt[x] += 1
        return ans