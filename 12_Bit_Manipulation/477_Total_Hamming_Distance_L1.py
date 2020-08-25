class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for n in zip(*map('{:032b}'.format, nums)):
            ans += n.count('1') * n.count('0')
        return ans