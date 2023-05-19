""" https://leetcode.com/problems/number-of-matching-subsequences/
1. For saving time, we can preprocess the string to get indexes of all the characters in the string using hash table.
2. Then, use two pointers to find the left most valid character in every chacters of the word.

Time complexity: O(TlogS), where T is the sum of word length and S is string length.

"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = defaultdict(list)
        for i, c in enumerate(s): mp[c].append(i)
        
        ans = 0
        for w in words:
            i = 0
            for c in w:
                j = bisect_left(mp[c], i)
                if j==len(mp[c]): break
                i = mp[c][j]+1
            else: ans += 1
        return ans