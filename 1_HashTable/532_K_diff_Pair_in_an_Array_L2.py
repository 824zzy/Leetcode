""" https://leetcode.com/problems/k-diff-pairs-in-an-array/
Let us just use counter and count frequency of each number in our array. We can have two options:
1. k > 0, it means, that for each unique number i we are asking if number i+k also in table.
2. k = 0, it means, that we are looking for pairs of equal numbers, so just check each frequency.
"""
class Solution:
    def findPairs(self, A: List[int], k: int) -> int:
        cnt = Counter(A)
        if k>0:
            ans = sum([i+k in cnt for i in cnt])
        elif k==0: ans = sum([cnt[i]>1 for i in cnt])
        return ans