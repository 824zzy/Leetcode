""" https://leetcode.com/problems/substring-with-concatenation-of-all-words/
apply l times sliding window to find all substrings
"""


class Solution:
    def findSubstring(self, A: str, words: List[str]) -> List[int]:
        l = len(words[0])
        n = len(words)
        words = Counter(words)
        ans = []
        for i in range(l):
            cnt = Counter()
            ii = i
            for j in range(i, len(A), l):
                word = A[j:j + l]
                cnt[word] += 1
                while cnt[word] > words.get(word, 0):
                    cnt[A[ii:ii + l]] -= 1
                    ii += l
                if j + l - ii == l * n:
                    ans.append(ii)
        return ans
