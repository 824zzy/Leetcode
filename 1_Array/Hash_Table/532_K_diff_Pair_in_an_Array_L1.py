class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        pairs = {}
        seen = set()
        for i, n in enumerate(nums):
            pairs[n] = i
            
        for i, n in enumerate(nums):
            if n+k in pairs and (n,n+k) not in seen and pairs[n+k]!=i:
                seen.add((n, n+k))
                ans += 1
        return ans