class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            if all([w in allowed for w in word]): ans += 1
        return ans