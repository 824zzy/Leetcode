# KMP (Knuth-Morris-Pratt) Pattern Matching

## When to Use

| Problem Signal | Technique |
|---|---|
| Find pattern in text (exact match) | KMP or Z-function |
| Multiple pattern searches (reuse LPS) | KMP (build LPS once) |
| Need prefix-suffix information | KMP (LPS array has semantic meaning) |
| Find longest prefix that is also suffix | LPS array directly |
| Shortest palindrome (prepend chars) | KMP on `s + "#" + reverse(s)` |
| Periodic string detection | KMP (check `len % (len - lps[-1]) == 0`) |
| Find all occurrences of pattern | KMP (continue after match) |
| Pattern matching in transformed input | Z-function (simpler to reason about) |
| Need to find duplicates of variable length | Rolling hash + binary search |
| Approximate matching / fuzzy search | Not KMP (use edit distance) |

### KMP vs Z-function vs Rolling Hash

**KMP:**
- Best when you care about prefix-suffix structure or need to reuse the pattern preprocessing.
- Provides explicit semantic meaning (LPS array tells you fallback positions).
- O(n + m) time, O(m) space.

**Z-function:**
- Best when you need to concat pattern and text (`pattern + $ + text`) and find all matches.
- Simpler mental model for "how far does this position match from the start?"
- O(n + m) time, O(n + m) space.
- Often more elegant for one-off pattern searches.

**Rolling hash:**
- Best when finding variable-length duplicates or when you need to compare many substrings quickly.
- Probabilistic (hash collisions), needs collision resolution.
- Works well with binary search (e.g., longest duplicate substring).
- O(n) per query after O(n) preprocessing.

## Pattern Matching Template

Find first occurrence of `pattern` in `text`. Returns index or -1.

```py
def getLPS(s):
    """Build longest prefix suffix array for pattern matching."""
    i = 0
    lps = [0] * len(s)
    for j in range(1, len(s)):
        while s[j] != s[i] and i:
            i = lps[i - 1]
        if s[j] == s[i]:
            i += 1
        lps[j] = i
    return lps

def kmp_search(text, pattern):
    """Find first occurrence of pattern in text."""
    lps = getLPS(pattern)
    i = 0
    for j in range(len(text)):
        while text[j] != pattern[i] and i:
            i = lps[i - 1]
        if text[j] == pattern[i]:
            i += 1
        if i == len(pattern):
            return j - len(pattern) + 1
    return -1
```

**Complexity:** O(n + m) time, O(m) space where n = len(text), m = len(pattern).

## Understanding the LPS Array

The LPS (Longest Prefix Suffix) array is the core of KMP. For each position `i`:

```
lps[i] = length of longest proper prefix of s[0..i] that is also a suffix of s[0..i]
```

**Example:** `s = "AABAAC"`
```
i:     0  1  2  3  4  5
s[i]:  A  A  B  A  A  C
lps:   0  1  0  1  2  0
```

At `i=4`: `s[0..4] = "AABAA"`. Longest prefix that is also suffix is `"AA"` (length 2).

**Key insight:** When a mismatch happens at position `i`, `lps[i-1]` tells you the next position in the pattern to try (already matched a prefix of that length).

## LPS Array Applications Beyond Pattern Matching

### 1. Longest Happy Prefix (LC 1392)

Find the longest string that is both prefix and suffix (but not the whole string).

```py
def longestPrefix(s: str) -> str:
    lps = getLPS(s)
    return s[:lps[-1]]
```

**Insight:** `lps[-1]` directly gives you the answer.

### 2. Shortest Palindrome (LC 214)

Prepend minimum chars to make a palindrome. Find the longest prefix that matches a suffix of the reverse.

```py
def shortestPalindrome(s: str) -> str:
    ss = s + "#" + s[::-1]
    lps = getLPS(ss)
    return s[lps[-1]:][::-1] + s
```

**Insight:** The separator `#` prevents overlaps. `lps[-1]` tells you how much of the original string is already palindromic from the start.

### 3. Repeated Substring Pattern (LC 459)

Check if the string is formed by repeating a substring.

```py
def repeatedSubstringPattern(s: str) -> bool:
    lps = getLPS(s)
    n = len(s)
    return lps[-1] > 0 and n % (n - lps[-1]) == 0
```

**Insight:** If `s` is periodic with period `p`, then `lps[-1] = n - p`. Check if `n` is divisible by `p`.

**Why it works:**
- If `lps[-1] = k`, then the last `k` characters match the first `k` characters.
- Period `p = n - k`. For full repetition, `n` must be a multiple of `p`.

### 4. Detect All Occurrences of Pattern

Don't return on first match; reset to `lps[i-1]` and continue.

```py
def find_all_occurrences(text, pattern):
    lps = getLPS(pattern)
    i = 0
    matches = []
    for j in range(len(text)):
        while text[j] != pattern[i] and i:
            i = lps[i - 1]
        if text[j] == pattern[i]:
            i += 1
        if i == len(pattern):
            matches.append(j - len(pattern) + 1)
            i = lps[i - 1]  # continue searching
    return matches
```

### 5. String Rotation (LC 796)

Check if `s` is a rotation of `goal`. A rotation means `s` appears in `goal + goal`.

```py
def rotateString(s: str, goal: str) -> bool:
    return len(s) == len(goal) and s in goal + goal
```

**KMP variant (overkill but valid):**

```py
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    return kmp_search(goal + goal, s) != -1
```

## LeetCode Problems

| Problem | Difficulty | Key Insight |
|---------|-----------|-------------|
| [28. Find the Index of the First Occurrence](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | L1 | Direct KMP template |
| [796. Rotate String](https://leetcode.com/problems/rotate-string/) | L0 | Check if s in goal+goal |
| [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | L1 | Check `len % (len - lps[-1]) == 0` |
| [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | L1 | Return `s[:lps[-1]]` |
| [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | L2 | KMP on `s + # + reverse(s)` |

## Common Pitfalls

**Pitfall 1: Off-by-one in index calculation**

When a match completes at position `j`, the starting index is `j - len(pattern) + 1`, not `j - len(pattern)`.

**Pitfall 2: Forgetting to reset after match**

If you need all occurrences, reset to `lps[i-1]` after a match, not `i = 0`.

**Pitfall 3: Modifying pattern matching logic for array comparisons**

KMP works on any comparable sequence. For array problems (LC 3036), transform to integers first:

```py
# Convert array comparisons to comparable values
def compare(x, y):
    return 1 if y > x else (0 if y == x else -1)

transformed = [compare(A[i], A[i+1]) for i in range(len(A)-1)]
# Now run KMP on transformed sequence
```

## Reference

- [Hiepit's KMP Template](https://leetcode.com/problems/subtree-of-another-tree/discuss/474425/JavaPython-2-solutions%3A-Naive-Serialize-in-Preorder-then-KMP-O(M%2BN)-Clean-and-Concise)
- [KMP Algorithm Explanation](https://www.youtube.com/watch?v=GTJr8OvyEVQ)
