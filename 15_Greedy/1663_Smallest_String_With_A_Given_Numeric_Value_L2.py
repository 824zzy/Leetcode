class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        x = k - n
        ans = 'z' * (x // 25)
        x %= 25
        if x: ans = chr(ord('a')+x) + ans
        return 'a'*(n-len(ans))+ans