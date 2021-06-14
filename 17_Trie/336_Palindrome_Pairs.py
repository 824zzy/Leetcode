""" L2:
"""
class Trie: 
    def __init__(self): 
        self.root = {}
    
    def insert(self, word, k): 
        node = self.root 
        for i, c in enumerate(word): 
            if word[i:] == word[i:][::-1]: node.setdefault("val", []).append(k)
            node = node.setdefault(c, {})
        node.setdefault("val", []).append(k)
        node.setdefault("end", []).append(k)
            
    def search(self, word): 
        ans = []
        node = self.root
        for i, c in enumerate(word): 
            if word[i:] == word[i:][::-1]: ans.extend(node.get("end", []))
            if c not in node: break 
            node = node[c]
        else: ans += node.get("val", [])
        return ans 
    

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words): 
            trie.insert(word, i)
        
        ans = set()
        for i, word in enumerate(words): 
            val = trie.search(word[::-1])
            for ii in val: 
                if ii != i: ans.add((ii, i))
        return ans 