class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums, prev_i=1):
            if not nums: self.ans += 1
            for cur_i, n in enumerate(nums):
                if prev_i%n==0 or n%prev_i==0:
                    dfs(nums[:cur_i]+nums[cur_i+1:], prev_i+1)
        dfs(nums)
        return self.ans