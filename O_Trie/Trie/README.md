# Trie

## When to Use

| Problem Signal | Technique |
|---|---|
| Prefix/suffix matching in string dictionary | Standard trie |
| Count words with prefix / prefix scores | Trie with counters on each node |
| Autocomplete / search suggestions | Trie + DFS to collect top k results |
| Add/search with wildcards (`.` matches any char) | Trie + backtracking |
| Match reversed string patterns (suffix matching) | Suffix trie (insert reversed strings) |
| Prefix and suffix queries on same word | Combined trie (insert `suffix$prefix` keys) |
| Find all words in 2D board | Trie + DFS with pruning |
| Maximize XOR of two numbers | Bitwise trie (binary representation) |
| Count pairs with XOR in range | Bitwise trie with counters |
| XOR queries with constraints (e.g., value <= m) | Bitwise trie + sorted insertion |

## Standard Trie

### Full Class Template

```py
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

### Contest Shorthand

```py
trie = {}
for word in words:
    node = trie
    for c in word:
        node = node.setdefault(c, {})
    node['#'] = word
```

## Common Variants

### Trie with Counter (Prefix Scores)

LC 208, 2416

Store counts at each node to track how many words pass through that prefix.

```py
root = {}
for word in words:
    node = root
    for c in word:
        node = node.setdefault(c, {})
        node['#'] = node.get('#', 0) + 1

# query: sum scores for all prefixes of a word
score = 0
node = root
for c in word:
    node = node[c]
    score += node['#']
```

### Suffix Trie (Reversed Strings)

LC 820, 336

Insert reversed strings to enable suffix matching.

```py
trie = {}
for word in words:
    node = trie
    for c in reversed(word):
        node = node.setdefault(c, {})
    node['#'] = word
```

**Trick for palindrome pairs (LC 336):** Store indices where remaining suffix/prefix is itself a palindrome.

```py
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word, k):
        node = self.root
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                node.setdefault('val', []).append(k)
            node = node.setdefault(c, {})
        node.setdefault('val', []).append(k)
        node.setdefault('end', []).append(k)

    def search(self, word):
        ans = []
        node = self.root
        for i, c in enumerate(word):
            if word[i:] == word[i:][::-1]:
                ans.extend(node.get('end', []))
            if c not in node:
                break
            node = node[c]
        else:
            ans += node.get('val', [])
        return ans
```

### Combined Prefix-Suffix Trie

LC 745

For queries like "find word with prefix=X and suffix=Y", insert all rotations.

For word "test", insert: "#test", "t#test", "st#test", "est#test", "test#test".

Query with `suffix + "$" + prefix`.

```py
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, i, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node['#'] = i
            node = node[c]
        node['#'] = i

    def search(self, word):
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return -1
        return node['#']

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            for k in range(len(word)):
                key = word[k:] + "$" + word
                self.trie.insert(i, key)

    def f(self, prefix: str, suffix: str) -> int:
        key = suffix + "$" + prefix
        return self.trie.search(key)
```

### Trie + Backtracking (Wildcards)

LC 211

Allow `.` to match any character by branching to all children.

```py
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            if word[i] == '.':
                return any(dfs(i + 1, child) for c, child in node.items() if c != '#')
            if word[i] not in node:
                return False
            return dfs(i + 1, node[word[i]])

        return dfs(0, self.trie)
```

### Trie + DFS (Word Search II)

LC 212

Build trie from words, then DFS the board. Prune matched words and leaf nodes.

```py
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word

        def dfs(p, x, y):
            node = p[board[x][y]]
            if '#' in node:
                ans.append(node['#'])
                node.pop('#')  # avoid duplicates
            tmp = board[x][y]
            board[x][y] = '!'  # mark visited
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in node:
                    dfs(node, nx, ny)
            board[x][y] = tmp
            # prune leaf nodes
            if not node:
                p.pop(board[x][y])

        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(trie, i, j)
        return ans
```

## Bitwise Trie

For XOR maximization/range problems. Insert binary representations (usually 32 bits).

### Template

```py
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in map(int, word):
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = int(word, 2)
```

### Maximum XOR of Two Numbers

LC 421

Build trie from all numbers. For each number, greedily choose the opposite bit at each level.

```py
class Solution:
    def findMaximumXOR(self, A: List[int]) -> int:
        T = Trie()
        for x in A:
            T.insert(bin(x)[2:].zfill(32))

        ans = 0
        for x in A:
            node = T.trie
            for c in map(int, bin(x)[2:].zfill(32)):
                # prefer opposite bit
                node = node.get(1 - c) or node.get(c)
            ans = max(ans, x ^ node['#'])
        return ans
```

### XOR with Constraint (Value <= m)

LC 1707

Sort both array and queries. Build trie incrementally to only include valid elements.

```py
class Solution:
    def maximizeXor(self, A: List[int], queries: List[List[int]]) -> List[int]:
        A.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        T = Trie()

        ans = [-1] * len(queries)
        k = 0
        for m, x, idx in queries:
            while k < len(A) and A[k] <= m:
                T.insert(bin(A[k])[2:].zfill(32))
                k += 1
            node = T.trie
            if not node:
                continue
            for c in map(int, bin(x)[2:].zfill(32)):
                node = node.get(1 - c) or node.get(c)
            ans[idx] = x ^ node['#']
        return ans
```

### Bitwise Trie with Counter (XOR Range Count)

LC 1803

Store counts at each node to enable range queries. Not yet implemented in this repo.

## Key Insights

### Space-time tradeoff
Trie uses O(N * L) space where N = number of words, L = average length. This beats O(N * L) search time for naive string matching.

### End marker convention
Use `'#'` to mark word endings. Can store the word itself, an index, or a count.

### setdefault shorthand
`node = node.setdefault(c, {})` is equivalent to:
```py
if c not in node: node[c] = {}
node = node[c]
```

### Pruning in board search
For LC 212, pruning is critical to avoid TLE:
1. Pop `'#'` after finding a word to avoid duplicates.
2. Remove empty child nodes after backtracking.

### Binary representation padding
Always use `.zfill(32)` for bitwise tries to ensure consistent structure.

## LeetCode Problems

### Standard Trie
- LC 208: Implement Trie (Prefix Tree)
- LC 677: Map Sum Pairs
- LC 648: Replace Words
- LC 720: Longest Word in Dictionary
- LC 1233: Remove Sub-Folders from Filesystem
- LC 1268: Search Suggestions System
- LC 1032: Stream of Characters (suffix trie)

### Trie Variants
- LC 211: Design Add and Search Words Data Structure (wildcards)
- LC 676: Implement Magic Dictionary (one char diff)
- LC 745: Prefix and Suffix Search (combined trie)
- LC 820: Short Encoding of Words (suffix trie)
- LC 1804: Implement Trie II (with count)
- LC 2416: Sum of Prefix Scores of Strings (prefix count)
- LC 2261: K Divisible Elements Subarrays (trie for deduplication)
- LC 2227: Encrypt and Decrypt Strings (reverse lookup)

### Advanced
- LC 212: Word Search II (trie + DFS + pruning)
- LC 336: Palindrome Pairs (suffix trie with palindrome indices)
- LC 386: Lexicographical Numbers (implicit trie traversal)

### Bitwise Trie
- LC 421: Maximum XOR of Two Numbers in an Array
- LC 1707: Maximum XOR With an Element From Array (sorted insertion)
- LC 1803: Count Pairs With XOR in a Range (trie + counter)
