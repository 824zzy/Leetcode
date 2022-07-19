""" https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/
1. compute prefix sum with modulo
2. if a prefix is already seen, that means **all the subarray that it represents can divisible by k**.
"""
# online solution
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

# offline solution
class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        prefix = list(accumulate(A, initial=0))
        seen = Counter()
        ans = 0
        
        for x in prefix:
            x %= k 
            ans += seen[x]
            seen[x] += 1
        return ans