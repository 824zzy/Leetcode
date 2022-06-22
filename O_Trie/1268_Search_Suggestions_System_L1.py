""" https://leetcode.com/problems/search-suggestions-system/
build a trie while maintain a set of words of every prefix.

Time complexity: O(n*l), where n=len(p), l=max(product_length)
"""
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node: 
                node[c] = {}
                node[c]['#'] = set()
            node[c]['#'].add(word)
            node = node[c]
        if '#' not in node: node['#'] = set([word])
        else: node['#'].add(word)
        
    def search(self, word):
        node = self.trie
        for c in word:
            if c not in node: return []
            node = node[c]
        if len(node['#'])>=3: return sorted(node['#'])[:3]
        else: return sorted(node['#'])
        
        
class Solution:
    def suggestedProducts(self, P: List[str], s: str) -> List[List[str]]:
        T = Trie()
        for w in P: T.insert(w)
        
        ans = []
        for i in range(len(s)):
            ans.append(T.search(s[:i+1]))
        return ans