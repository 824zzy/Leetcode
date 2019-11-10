# Google
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n_set = set(nums)
        n_all_set = set([i for i in range(1, len(nums)+1)])
        return list(n_all_set-n_set)
        