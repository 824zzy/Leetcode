""" https://leetcode.com/problems/design-add-and-search-words-data-structure/
trie + dfs
"""
class WordDictionary:
    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, A: str) -> bool:
        def dfs(node, i):
            if i==len(A): return node.get('#', False)
            
            if A[i]=='.': return any([dfs(v, i+1) for k, v in node.items() if k!='#'])
            else: return A[i] in node and dfs(node[A[i]], i+1)
            
        return dfs(self.trie, 0)