# Brain teaser
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        elif s==s[::-1]: return 1
        else: return 2