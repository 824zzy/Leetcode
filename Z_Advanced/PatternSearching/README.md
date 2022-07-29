# Pattern Searching

## Template

``` py
""" find the index of pattern in string, if pattern not in string then return -1
p: pattern
s: string
LPS: longest prefix suffix
"""
def getLPS(s):
    i = 0
    lps = [0] * len(s)
    for j in range(1, len(s)):
        while s[j]!=s[i] and i: i = lps[i-1]
        if s[j] == s[i]: i += 1
        lps[j] = i
    return lps

lps = getLPS(p)
i = 0
for j in range(len(s)):
    while s[j]!=p[i] and i: i = lps[i-1]
    if s[j]==p[i]: i += 1
    if i==len(p): return j-len(p)+1
return -1
```

## Reference

- [Hiepit's template](https://leetcode.com/problems/subtree-of-another-tree/discuss/474425/JavaPython-2-solutions%3A-Naive-Serialize-in-Preorder-then-KMP-O(M%2BN)-Clean-and-Concise)
