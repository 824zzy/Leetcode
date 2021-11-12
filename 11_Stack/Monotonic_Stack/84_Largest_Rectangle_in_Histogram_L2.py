class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        s, ans = [], 0
        for i, h in enumerate(A+[0]):
            while s and h<=A[s[-1]]:
                H = A[s.pop()]
                W = i if not s else i-s[-1]-1
                ans = max(ans, H*W)
            s.append(i)
        return ans