# Straight forward template solution
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        ans = [p for p in prices]
        for i, p in enumerate(prices):
            while s and p<=s[-1][-1]:
                idx, val = s.pop()
                ans[idx] = val-p
            s.append((i, p))
        return ans

# Space optimized solution
class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
        s = []
        for i, p in enumerate(A):
            while s and A[i]<=A[s[-1]]:
                idx = s.pop()
                A[idx] -= A[i]
            s.append(i)
        return A