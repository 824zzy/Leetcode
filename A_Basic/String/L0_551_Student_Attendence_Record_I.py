class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        elif 'LLL' in s:
            return False
        return True
