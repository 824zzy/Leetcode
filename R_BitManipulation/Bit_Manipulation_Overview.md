---
tags:
  - leetcode
  - bitmanipulation
  - moc
---

# Bit Manipulation

## When to Use

| Problem Signal | Technique |
|---|---|
| Count set bits (1s), check parity | Basic bit operations (AND, shift) |
| Find single/missing number with XOR constraint | XOR properties (self-inverse, commutative) |
| Test if power of 2, isolate lowest set bit | `x & (x-1)` and `x & -x` tricks |
| Generate all subsets, iterate states | Bitmask enumeration (`range(1<<n)`) |
| DP on subsets (assign items to groups, min cost with state) | Bitmask DP with memoization |
| Check if two sets overlap (e.g., strings share chars) | String to bitmask + AND test |
| Maximum XOR queries, prefix matching | Greedy bit-by-bit construction |
| Range bitwise AND/OR | Find common prefix (AND) or track set bits (OR) |
| Gray code, reflect subproblems | Gray code formula `(i>>1)^i` |
| Encode characters, fast set membership | Character bitmask (26 bits for lowercase) |

## Basic Bit Operations

### Get/Set/Flip Individual Bits

LC 191, 231, 461, 476, 1009

```py
# Get lowest bit (check odd/even)
x & 1

# Get i-th bit (0-indexed from right)
(x >> i) & 1

# Set i-th bit to 1
x | (1 << i)

# Flip i-th bit
x ^ (1 << i)

# Clear i-th bit
x & ~(1 << i)
```

### Isolate and Clear Lowest Set Bit

Key insight: `x & -x` isolates the lowest 1 bit. `x & (x-1)` clears it. These are the two most common bit tricks.

LC 191, 231, 260, 338

```py
# Get lowest "1" bit (useful for splitting by parity)
x & -x

# Clear lowest "1" bit (useful for counting set bits)
x & (x - 1)

# Count set bits (Brian Kernighan's algorithm)
def count_bits(x):
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt

# Alternative: Python built-in
x.bit_count()  # Python 3.10+
bin(x).count('1')
```

### Check Power of Two

LC 231, 342

```py
# x is power of 2 if it has exactly one set bit
def is_power_of_two(x):
    return x > 0 and x & (x - 1) == 0
```

### Bit Length and Masks

```py
# Get bit length (position of highest set bit + 1)
x.bit_length()

# 32-bit mask (all 1s)
0xffffffff

# n-bit mask (all 1s)
(1 << n) - 1

# Flip all bits in n-bit number
x ^ ((1 << n) - 1)

# Keep only odd position bits (1st, 3rd, 5th...)
x & 0x55555555  # binary: 0101...0101
```

## XOR Properties and Tricks

Key insight: XOR is self-inverse (`a ^ a = 0`), commutative, and associative. This makes it perfect for finding missing/unique elements.

### Find Missing/Unique Elements

LC 136, 137, 260, 268, 1734

**Single number (all others appear twice):**

```py
def singleNumber(nums):
    return reduce(xor, nums, 0)
```

**Two single numbers (all others appear twice):**

```py
def singleNumber(nums):
    diff = reduce(xor, nums, 0)
    diff &= -diff  # isolate lowest set bit
    ans = [0, 0]
    for x in nums:
        if diff & x:
            ans[0] ^= x
        else:
            ans[1] ^= x
    return ans
```

**XOR from 1 to n (pattern repeats every 4):**

```py
def xor_1_to_n(n):
    return [n, 1, n + 1, 0][n % 4]
```

**Decode XOR-encoded array:**

LC 1734

```py
def decode(encoded):
    n = len(encoded) + 1
    total = reduce(xor, range(1, n + 1))
    odd = reduce(xor, encoded[1::2])
    perm = [total ^ odd]
    for e in encoded:
        perm.append(perm[-1] ^ e)
    return perm
```

### XOR Prefix for Maximum Queries

LC 421, 1738

Key insight: to maximize XOR, try to build the opposite bit pattern from high to low.

**Maximum XOR of two numbers (greedy bit-by-bit):**

```py
def findMaximumXOR(nums):
    ans = 0
    for i in reversed(range(32)):
        ans <<= 1
        prefixes = {x >> i for x in nums}
        for p in prefixes:
            if ans ^ 1 ^ p in prefixes:
                ans += 1
                break
    return ans
```

## Range Bitwise Operations

### Range Bitwise AND

LC 201

Key insight: AND of a range is the common prefix of the binary representations.

```py
def rangeBitwiseAnd(m, n):
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift
```

### Subarray Bitwise ORs

LC 898

Key insight: OR can only set bits, never unset. So the number of distinct ORs ending at each position is bounded by O(log max(A)).

```py
def subarrayBitwiseORs(A):
    ans, vals = set(), set()
    for x in A:
        vals = {x | xx for xx in vals} | {x}
        ans |= vals
    return len(ans)
```

## Bitmask Enumeration

### Iterate All Subsets (Powerset)

LC 78, 1863, 2044

Key insight: use integers 0 to 2^n - 1 to represent all subsets.

```py
# Generate all subsets
def subsets(nums):
    ans = []
    for mask in range(1 << len(nums)):
        ans.append([nums[i] for i in range(len(nums)) if mask >> i & 1])
    return ans

# Alternative: check bit with left shift
def subsets(nums):
    ans = []
    for mask in range(1 << len(nums)):
        ans.append([nums[i] for i in range(len(nums)) if mask & (1 << i)])
    return ans
```

### String to Bitmask (Character Set Encoding)

LC 318, 1178, 2135

Key insight: encode which characters appear using a 26-bit integer (for lowercase a-z).

```py
# Encode string as bitmask
def string_to_mask(s):
    mask = 0
    for c in s:
        mask |= 1 << (ord(c) - ord('a'))
    return mask

# Check if two strings share characters
def no_overlap(s1, s2):
    return not (string_to_mask(s1) & string_to_mask(s2))
```

**Maximum product of word lengths:**

LC 318

```py
def maxProduct(words):
    masks = {}
    for w in words:
        mask = 0
        for c in w:
            mask |= 1 << (ord(c) - ord('a'))
        masks[mask] = max(masks.get(mask, 0), len(w))

    ans = 0
    for x in masks:
        for y in masks:
            if not (x & y):
                ans = max(ans, masks[x] * masks[y])
    return ans
```

## Bitmask Dynamic Programming

Key insight: when n is small (n <= 20), use an integer to represent which items are selected. Transition by flipping bits.

### Template: Top-Down DP

LC 698, 1125, 1434, 1494, 1659, 1681, 1947, 1986, 2305

```py
@cache
def dp(mask):
    if mask == 0:
        return base_case

    # Try removing each set bit
    for i in range(n):
        if mask & (1 << i):
            # Transition by clearing i-th bit
            result = combine(result, dp(mask ^ (1 << i)))

    return result

# Start with all bits set
return dp((1 << n) - 1)
```

### Template: Bottom-Up DP

```py
dp = [init_value] * (1 << n)
dp[0] = base_case

for mask in range(1 << n):
    if dp[mask] == init_value:
        continue
    for i in range(n):
        if mask & (1 << i):
            # Transition by clearing i-th bit
            new_state = mask ^ (1 << i)
            dp[mask] = combine(dp[mask], dp[new_state])
```

### Common Patterns

**Partition into k equal-sum subsets:**

LC 698

```py
@cache
def dp(mask):
    if mask == 0:
        return 0
    for j in range(n):
        if mask & (1 << j):
            prev = dp(mask ^ (1 << j))
            if prev >= 0 and prev + nums[j] <= target:
                return (prev + nums[j]) % target
    return -1

return dp((1 << n) - 1) == 0
```

**Smallest sufficient team (min subset cover):**

LC 1125

```py
@cache
def dp(i, mask):
    if mask == 0:
        return []
    if i == len(people):
        return [0] * 100  # impossible
    if not (mask & person_masks[i]):
        return dp(i + 1, mask)  # skip if no new skills
    # Take or skip person i
    return min(dp(i + 1, mask),
               [i] + dp(i + 1, mask & ~person_masks[i]),
               key=len)

return dp(0, (1 << num_skills) - 1)
```

**Iterate only valid states (pruning):**

LC 1349 (max students in exam with adjacency constraints)

```py
# Pre-filter valid row masks
valid = []
for mask in range(1 << n):
    if is_valid(mask):  # e.g., no adjacent bits set
        valid.append(mask)

@cache
def dp(row, prev_mask):
    if row == m:
        return 0
    ans = 0
    for mask in valid:
        if compatible(mask, prev_mask):
            ans = max(ans, popcount(mask) + dp(row + 1, mask))
    return ans
```

## Gray Code

LC 89

Key insight: Gray code for integer i is `(i >> 1) ^ i`. This ensures consecutive codes differ by exactly one bit.

```py
def grayCode(n):
    return [(i >> 1) ^ i for i in range(1 << n)]
```

## Python Bit Manipulation Functions

```py
# Binary representation
bin(x)  # returns '0b...'

# Parse binary string
int('1010', 2)  # returns 10

# Format as 32-bit binary string
format(x, '032b')
'{0:032b}'.format(x)
bin(x)[2:].zfill(32)

# Count set bits
x.bit_count()  # Python 3.10+
bin(x).count('1')

# Bit length (highest bit position + 1)
x.bit_length()
```

## Reference

- [Bitmask DP problem list](https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained)
- [从集合论到位运算，常见位运算技巧分类总结！](https://leetcode.cn/circle/discuss/CaOJ45/)
