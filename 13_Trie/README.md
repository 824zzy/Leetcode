# Trie Template

## Ultimate template for Prefix/Suffix Trie

``` py
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        Eg: ABCD vs AB
        """
        node = self.trie
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True
    
    def containsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that contains by the given prefix.
        Eg: ABCD vs ABCDE
        """
        node = self.trie
            for c in word:
                if c not in node: return False
                node = node[c]
                if '#' in node: return node['#']
    
```