class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        reversed_prefix = {}
        prefix = 0
        ans = float('inf')
        for i, n in enumerate(nums[::-1]):
            if prefix<x:
                prefix += n
                reversed_prefix[prefix] = i+1
                if prefix==x:
                    ans = min(ans, i+1)
        prefix = 0
        for i, n in enumerate(nums):
            if prefix<x:
                prefix += n
                if n==x:
                    ans = min(ans, i+1)
                elif x-prefix in reversed_prefix and i+reversed_prefix[x-prefix]<len(nums):
                    ans = min(ans, i+reversed_prefix[x-prefix]+1)
        return ans if ans!=float('inf') else -1