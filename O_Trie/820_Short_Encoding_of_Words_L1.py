""" https://leetcode.com/problems/short-encoding-of-words/
1. sort the words by length
2. use suffix trie to store all the reversed words while sum up the word lengths which are not a prefix of any words.

Due to the small data size and word length(7), brute force solutions #2 #3 also work.
"""
# trie along with longest word length
class Trie:
    def __init__(self):
        self.trie = {}
        self.len = 0
        
    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        if not node: 
            node['#'] = word
            self.len += len(word)+1
        
class Solution:
    def minimumLengthEncoding(self, words):
        words.sort(key=len, reverse=True)
        T = Trie()
        for w in words: T.insert(w[::-1])
        return T.len



# from lee: Time complexity: O(n*k*k)
class Solution:
    def minimumLengthEncoding(self, words):
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)
        
        
# Time complexity: O(n*n*k)
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        A = sorted(words, key=len, reverse=True)
        seen = set()
        for x in A:
            nxt_seen = set()
            if not seen: seen.add(x)
            else:
                for y in seen:
                    if y.endswith(x): break
                else: nxt_seen.add(x)
                seen |= nxt_seen
        return len(''.join(seen))+len(seen)
        