# Trie Template

## Ultimate template for Prefix/Suffix Trie

``` py
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix AB.
        Eg: ABCD vs AB(prefix)
        """
        node = self.trie
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True
    
    def containsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that contains by the given prefix ABCDE.
        Eg: ABCD vs ABCDE(prefix)
        """
        node = self.trie
        for c in word:
            if c not in node: return False
            node = node[c]
            if '#' in node: return node['#']    
```

## Simple version for contest

``` py
trie = {}
for word in words:
    node = trie
    for c in word:
        node = node.setdefault(c, {})
    node['#'] = word
```
