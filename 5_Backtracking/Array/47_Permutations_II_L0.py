# A tricky one line permutation by permutation
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(left, curr):
            if not left and curr not in self.ans:
                self.ans.append(curr)
                return
            for i in range(len(left)):
                dfs(left[:i]+left[i+1:], curr+[left[i]])
        dfs(nums, [])
        return self.ans
