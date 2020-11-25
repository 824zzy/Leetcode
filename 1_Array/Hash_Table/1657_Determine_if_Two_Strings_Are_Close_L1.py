class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values())==sorted(Counter(word2).values()) and Counter(word1).keys()==Counter(word2).keys()