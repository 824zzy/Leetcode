class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [i for i in range(1, n + 1)]
        for i in range(1, k):
            ans[i:] = ans[i:][::-1]
        return ans
