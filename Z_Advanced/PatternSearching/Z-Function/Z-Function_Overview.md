---
tags:
  - leetcode
  - advanced
  - moc
---

# Z-Function (Z-Algorithm)

## When to Use

| Problem Signal | Technique |
|---|---|
| Find pattern in text (exact match) | Z-function or KMP |
| Pattern matching on transformed/concatenated strings | Z-function (cleaner for one-off searches) |
| Count occurrences of pattern | Z-function on `pattern + "$" + text` |
| Find all prefix matches at every position | Z-function (core use case) |
| Sum of all LCP (longest common prefix) values | Z-function (LC 2223) |
| Check if suffix matches prefix | Z-function (LC 3031) |
| Periodic string / substring repetition | KMP or Z-function |
| Reuse pattern preprocessing multiple times | KMP (better semantic meaning) |

### KMP vs Z-function vs Rolling Hash

**Z-function:**
- Best when you concat pattern and text (`pattern + "$" + text`) and find all matches in one pass.
- Simpler mental model: "how long is the match starting at position i?"
- z[i] = length of longest substring starting at i that matches a prefix of the string.
- O(n) time, O(n) space.
- More elegant for one-off pattern searches or when you need all prefix match lengths.

**KMP:**
- Best when you care about prefix-suffix structure or need to reuse the pattern preprocessing.
- Provides explicit semantic meaning (LPS array tells you fallback positions).
- O(n + m) time, O(m) space (only pattern preprocessing stored).

**Rolling hash:**
- Best when finding variable-length duplicates or comparing many substrings quickly.
- Probabilistic (hash collisions), needs careful implementation.
- Works well with binary search (e.g., longest duplicate substring).
- O(n) per query after O(n) preprocessing.

## Z-Array Construction

The Z-array is the core data structure. For a string `s` of length n:

```
z[i] = length of longest substring starting at i that matches a prefix of s
```

By definition, `z[0]` is not well-defined (some set it to 0, some to n). The algorithm starts from `i=1`.

**Example:** `s = "aabcaab"`
```
i:    0  1  2  3  4  5  6
s[i]: a  a  b  c  a  a  b
z[i]: -  1  0  0  3  1  0
```

At `i=4`: starting from position 4, we have `"aab"` which matches the first 3 characters. So `z[4] = 3`.

## Z-Function Template

```py
def z_function(s):
    """Compute Z-array for string s.

    z[i] = length of longest substring starting at i that matches a prefix of s.
    z[0] is typically set to 0 (or left undefined).

    Time: O(n), Space: O(n)
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # [l, r] is the rightmost Z-box found so far
    for i in range(1, n):
        # Case 1: i is beyond the current Z-box, start fresh
        if i > r:
            z[i] = 0
        # Case 2: i is inside the Z-box, use previously computed value
        else:
            # z[i-l] is the corresponding position in the prefix
            # But we can only copy min(z[i-l], r-i+1) to avoid going past r
            z[i] = min(r - i + 1, z[i - l])

        # Try to extend the match
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update the Z-box if we extended past r
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z
```

**Key insight (the Z-box optimization):**

We maintain `[l, r]` as the interval with the rightmost `r` such that `s[l..r]` matches `s[0..r-l]`.

When processing position `i`:
- If `i <= r`, we know `s[i..r]` matches `s[i-l..r-l]`, so we can reuse `z[i-l]`.
- We still need to try extending past `r` to find the full match length.
- This amortization gives us O(n) total time.

**Complexity:** O(n) time, O(n) space.

## Pattern Matching with Z-Function

To find all occurrences of `pattern` in `text`:

1. Concatenate: `combined = pattern + "$" + text` where `$` is a separator not in the alphabet.
2. Compute Z-array for `combined`.
3. Any position `i` where `z[i] == len(pattern)` is an occurrence.

```py
def z_pattern_search(text, pattern):
    """Find all starting indices where pattern occurs in text."""
    combined = pattern + "$" + text
    z = z_function(combined)
    m = len(pattern)
    matches = []
    for i in range(m + 1, len(combined)):
        if z[i] == m:
            matches.append(i - m - 1)  # adjust for pattern and separator
    return matches
```

**Why it works:**
- If `z[i] == len(pattern)`, it means starting at position `i`, we have a full match with the prefix (which is the pattern).
- The separator `$` ensures the pattern itself doesn't create false positives by matching across the boundary.

**Complexity:** O(n + m) time, O(n + m) space.

## Common Use Cases

### 1. Count Pattern Occurrences (LC 3036)

For array-based pattern matching, transform comparisons to a comparable sequence first.

```py
def countMatchingSubarrays(A: List[int], pattern: List[int]) -> int:
    def compare(x, y):
        if y > x: return 1
        elif y == x: return 0
        else: return -1

    # Transform array differences
    transformed = [compare(A[i], A[i + 1]) for i in range(len(A) - 1)]

    # Pattern search
    combined = pattern + transformed  # no separator needed if pattern doesn't match itself
    z = z_function(combined)
    return sum(z[i] >= len(pattern) for i in range(len(pattern), len(combined)))
```

**Key insight:** Convert array comparison to integers, then run Z-function. Count positions where `z[i] >= len(pattern)`.

### 2. Sum of All Prefix Match Lengths (LC 2223)

For each suffix of the string, compute the length of its LCP with the original string and sum them up.

```py
def sumScores(s: str) -> int:
    z = z_function(s)
    return sum(z) + len(s)  # +len(s) accounts for z[0] (the full string)
```

**Insight:** The Z-array directly gives you the LCP for each suffix. Sum all values plus the string length itself.

### 3. Check if Suffix Matches Prefix (LC 3031)

Check if after removing the first `k` characters repeatedly, the remaining string matches a prefix of the original.

```py
def minimumTimeToInitialState(s: str, k: int) -> int:
    z = z_function(s)
    for i, match_len in enumerate(z):
        if i % k != 0:
            continue
        # Check if the remaining string matches a prefix
        if len(s) - i == match_len:
            return i // k
    return ceil(len(s) / k)
```

**Insight:** We only check positions that are multiples of `k`. If `z[i] == len(s) - i`, the entire suffix matches a prefix.

## Understanding the Z-Box

The Z-box `[l, r]` is the key optimization. It represents the rightmost segment `s[l..r]` that matches `s[0..r-l]`.

**Invariant:** At position `i`, we have `r >= i-1` (we've checked everything before `i`).

When `i <= r`:
- We know `s[i..r]` matches `s[i-l..r-l]` (since the whole `[l, r]` box matches the prefix).
- The mirror position `i-l` in the prefix tells us about `i`.
- We can copy `z[i-l]`, but cap it at `r-i+1` (we can't trust anything past `r` yet).

When we extend past `r`, we update the Z-box to reflect the new rightmost match.

**Why this is O(n):** The right pointer `r` only increases, and we do O(1) work per character. Total work is O(n).

## LeetCode Problems

| Problem | Difficulty | Key Insight |
|---------|-----------|-------------|
| [2223. Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) | L3 | Sum all Z-array values + n |
| [3031. Minimum Time to Revert Word to Initial State II](https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/) | L3 | Check `z[i] == n-i` at multiples of k |
| [3036. Number of Subarrays That Match a Pattern II](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/) | L3 | Transform array diffs, run Z-function |

## Common Pitfalls

**Pitfall 1: Forgetting the separator in pattern matching**

When concatenating `pattern + text`, you need a separator (like `$`) to prevent false matches across the boundary. Without it, the pattern might match with itself in unexpected ways.

**Pitfall 2: Off-by-one in index calculation**

When `z[i] == len(pattern)`, the match in the original text starts at `i - len(pattern) - 1` (accounting for the separator). Double-check your index arithmetic.

**Pitfall 3: Initializing z[0]**

The Z-array typically starts from `i=1` since `z[0]` is undefined (or set to 0 or n depending on convention). Make sure your algorithm doesn't depend on `z[0]`.

**Pitfall 4: Not capping z[i] at r-i+1**

Inside the Z-box, you must cap `z[i] = min(r - i + 1, z[i - l])`. If you just copy `z[i-l]`, you might use information beyond `r` that hasn't been verified yet.

## Reference

- [CP-Algorithms: Z-Function](https://cp-algorithms.com/string/z-function.html)
- [Codeforces Tutorial](https://codeforces.com/blog/entry/3107)
