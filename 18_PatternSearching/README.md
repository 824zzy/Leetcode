# Pattern Searching

## Template

``` py
def getLPS(s):
            m, j = len(s), 0
            lps = [0] * m
            for i in range(1, m):
                while s[i] != s[j] and j > 0: j = lps[j-1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps
        
def kmp(s, p):
    lps = getLPS(p)
    n, m, j = len(s), len(p), 0
    for i in range(n):
        while s[i] != p[j] and j > 0: j = lps[j-1]
        if s[i] == p[j]:
            j += 1
            if j == m: return True
    return False
```

## Reference

- [Hiepit's template](https://leetcode.com/problems/subtree-of-another-tree/discuss/474425/JavaPython-2-solutions%3A-Naive-Serialize-in-Preorder-then-KMP-O(M%2BN)-Clean-and-Concise)