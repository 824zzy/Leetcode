# Trie Template

## Prefix/Suffix Trie

``` py
trie = {}
for word in words:
    node = trie
    for ch in reversed(word):
        if ch not in node:
            node[ch] = {}
        node = node[ch]
```
