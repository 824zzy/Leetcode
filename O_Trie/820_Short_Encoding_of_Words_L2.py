# suffix trie + dfs
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        for word in words:
            node = trie
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
        
        def dfs(node, l):
            if not node: return l
            s = 0
            for c in node.values():
                s += dfs(c, l+1)
            return s    
        
        return dfs(trie, 1)