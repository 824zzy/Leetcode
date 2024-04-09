class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        ans = 0
        while i <= n:
            if n % i == 0:
                ans += 1
                if k == ans:
                    return i
            i += 1
        return -1
