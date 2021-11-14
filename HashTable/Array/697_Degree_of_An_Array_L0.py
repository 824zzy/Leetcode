from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        degree = max(cnt.values())
        cand = [k for k, v in cnt.items() if v==degree]
        ans = []
        for c in cand:
            l = nums.index(c)
            r = len(nums)-nums[::-1].index(c)-1
            ans.append(r-l+1)
        return min(ans)