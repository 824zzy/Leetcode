""" L3: https://leetcode.com/problems/count-vowel-substrings-of-a-string/
TODO: https://leetcode.com/problems/count-vowel-substrings-of-a-string/discuss/1563707/Python3-sliding-window-O(N)
due to the small data dize, brute force is available
"""
# brute force
class Solution:
    def countVowelSubstrings(self, A: str) -> int:
        ans = 0
        for i in range(len(A)):
            freq = Counter()
            for j in range(i, len(A)):
                if A[j] in "aeiou":
                    freq[A[j]] += 1
                    if len(freq)==5: ans += 1
                else: break
        return ans

# sliding window
class Solution:
    def countVowelSubstrings(self, A: str) -> int:
        freq = Counter()
        ans = 0
        for i in range(len(A)):
            if A[i] in "aeiou":
                if not i or A[i-1] not in "aeiou":
                    jj = j = i
                    freq.clear()
                freq[A[i]] += 1
                while len(freq)==5 and all(freq.values()):
                    freq[A[j]] -= 1
                    j += 1
                ans += j-jj
        return ans
                