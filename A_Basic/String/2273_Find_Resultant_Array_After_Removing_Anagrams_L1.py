""" https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
label the problem L1 due to the complex description
"""
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if not i or sorted(words[i])!=sorted(words[i-1]):
                ans.append(words[i])
        return ans