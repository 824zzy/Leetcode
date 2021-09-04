""" L1
"""
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(node):
            if node in self.seen: return
            self.seen.add(node)
            self.cnt += 1
            dfs(nums[node])

        ans = 0
        self.seen = set()
        for n in nums:
            self.cnt = 0
            dfs(n)
            ans = max(self.cnt, ans)
        return ans
