class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = {}
        def insert(word):
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = '#'
        
        def search(word):
            node = trie
            for c in word:
                if c not in node: return False
                node = node[c]
                if '#' not in node: return False
            return '#' in node
        
        for w in words: insert(w)
        words = sorted(words, key=lambda x: (-len(x), x))
        for w in words:
            if search(w): return w
        return ''