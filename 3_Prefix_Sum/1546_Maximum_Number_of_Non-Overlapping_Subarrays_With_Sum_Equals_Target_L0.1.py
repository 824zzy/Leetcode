class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cnt = collections.Counter()
        cnt[0] = 1
        ans = 0
        prefix = 0
        for n in nums:
            prefix += n
            if cnt[prefix-target]!=0:
                ans += 1
                cnt = collections.Counter()
            cnt[prefix] += 1
        return ans