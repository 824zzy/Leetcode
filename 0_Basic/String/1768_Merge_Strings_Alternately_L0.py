# Straightforward solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = list(word1), list(word2)
        ans = ''
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        return ans + ''.join(word1[i+1:]) if len(word1)>len(word2) else ans + ''.join(word2[i+1:])


# zip_longest function trick
 class Solution:
    def mergeAlternately(self, word1, word2):
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))