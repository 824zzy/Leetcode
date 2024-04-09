""" https://leetcode.com/problems/intervals-between-identical-elements/
"""


class Solution:
    def getDistances(self, A: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i, x in enumerate(A):
            mp[x].append(i)

        ans = [0] * len(A)
        for k, idx in mp.items():
            prefix = list(accumulate(idx, initial=0))
            for i, x in enumerate(idx):
                l = idx[i] * i - prefix[i]
                r = prefix[-1] - prefix[i] - (len(idx) - i) * idx[i]
                ans[idx[i]] = l + r
        return ans
