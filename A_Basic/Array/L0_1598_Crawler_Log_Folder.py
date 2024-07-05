class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for l in logs:
            if l == "../":
                if ans > 0:
                    ans -= 1
            elif l == "./":
                continue
            else:
                ans += 1
        return ans
