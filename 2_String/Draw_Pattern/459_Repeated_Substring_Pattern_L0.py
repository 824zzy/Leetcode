class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub = s[:i]
            # print(sub)
            if sub*(len(s)//i) == s:
                return True
        return False