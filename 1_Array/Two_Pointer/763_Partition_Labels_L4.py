# Amazon
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        l, r, ans = 0, 0, []
        rightMost = {c:i for i, c in enumerate(S)}
        for i, c in enumerate(S):
            r = max(r, rightMost[c])
            if i==r:
                ans.append(r-l+1)
                l = r + 1
        return ans