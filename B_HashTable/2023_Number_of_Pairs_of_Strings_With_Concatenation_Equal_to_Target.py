""" L1: use frequent table to find needed cancatenation
similar to two sum but when prefix equals to suffix, we need to minus duplicated count.
"""


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        cnt = Counter(nums)
        for k, v in cnt.items():
            if target.startswith(k):
                suffix = target[len(k):]
                ans += cnt[suffix] * v
                if k == suffix:
                    ans -= v
        return ans

# brute force


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        ans += 1
        return ans
