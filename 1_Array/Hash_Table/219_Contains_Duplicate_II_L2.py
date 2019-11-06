# Google
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexs = {}
        for i, n in enumerate(nums):
            if n in indexs:
                if i - indexs[n] <= k:
                    return True
            indexs[n] = i
        return False