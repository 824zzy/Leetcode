# Set or Hash Table all OK.
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        DNA, ans = set(), []
        for i in range(len(s)-9):
            if s[i:i+10] not in DNA:
                DNA.add(s[i:i+10])
            else:
                ans.append(s[i:i+10])
        return list(set(ans))