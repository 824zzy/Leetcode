class Solution:
    def minFlips(self, target: str) -> int:
        curr = '0'
        ans = 0
        for t in target:
            if t != curr:
                ans += 1
                curr = '0' if curr=='1' else '1'
        return ans