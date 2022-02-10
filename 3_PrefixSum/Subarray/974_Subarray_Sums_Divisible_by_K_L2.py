""" https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/
1. compute prefix sum with modulo
2. if a prefix is already seen, that means **all the subarray that it represents can divisible by k**.
"""
class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        seen = Counter()
        seen[0] = 1
        ans = 0
        prefix = 0
        
        for x in A:
            prefix = (prefix+x)%k
            ans += seen[prefix]
            seen[prefix] += 1
        return ans